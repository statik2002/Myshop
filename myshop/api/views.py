import json
import os
import pprint
import time

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.signing import Signer
from django.core import signing
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import CartSerializer, CatalogSerializer, CreateOrderProductSerializer, CustomerSerializer, FeedbackSerializer, OrderProductSerializer, OrderSerializer, ProductInCartSerializer, ProductInitialSerializer, ProductListSerializer, ProductQuestionSerializer, ProductSerializer
from main.models import Cart, Catalog, Customer, CustomerLoginFail, Feedback, Order, Product, ProductImage, ProductInCart, ProductInOrder, ProductQuestion
from main.email_functional import send_mail
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.db.models import Prefetch
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity

from myshop.settings import USER_BAN_HOURS

from main.slugify import slugify


class ProductViewSet(viewsets.ModelViewSet):
    """
        *** Get Products ***
        /api/v1/products/ - get all products (random order)
        /api/v1/products/{pk}/ - get product by pk

        *** Search products ***
            POST: /api/v1/products/search/
            JSON: {query: [search_param]}

        *** Update product ***
            PUT: /api/v1/products/{id}/
            JSON: {product}    
    """
    permission_classes = (AllowAny,)
    queryset = Product.objects.filter(quantity__gt=0).prefetch_related(Prefetch('product_feedbacks', queryset=Feedback.objects.filter(is_show=True))).order_by('?')
    serializer_class = ProductSerializer

    def retrieve(self, request, pk):
        product = Product.objects.get(pk=pk)
        return Response(ProductSerializer(product,  context={'request': request}).data, status=status.HTTP_200_OK)

    
    @action(detail=False, methods=['post'], name='search')
    def search(self, request):
        query = SearchQuery(request.data.get('query'))
        products = Product.objects.annotate(
            search=SearchVector('name')+SearchVector('description'),
            ).filter(search=query).filter(quantity__gt=0)
        page = self.paginate_queryset(products)
        if page is not None:
            serialized_products = ProductSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serialized_products.data)
        
        serialized_products = ProductSerializer(page, many=True, context={'request': request})
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['post'], name='upload_image')
    def upload_image(self, request):
        try:
            product = Product.objects.get(pk=request.data.get('product_id'))
            product_image = ProductImage.objects.create(
                product=product,
                alt=product.name,
                image=request.FILES.get('file')
            )
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    @action(detail=False, methods=['post'], name='delete_image')
    def delete_image(self, request):
        try:
            product_image = ProductImage.objects.get(pk=request.data.get('id'))
            path = product_image.image.path
            product_image.delete()
            os.remove(product_image.image.path)
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This image is absent!'}, status=status.HTTP_400_BAD_REQUEST)
        except OSError:
            return Response({'error': 'Can`t delete image file!'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)

    
    def get_permissions(self):
        if self.action in ['update', 'upload_image']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class InitialUploadCatalog(viewsets.ModelViewSet):

    """
        *** Upload catalog ***
        POST: /api/v1/initial_upload_catalog/
        HEADER: 'Authorization': f'Bearer {token}'
        JSON: {data: [catalog]}
    """

    permission_classes = (IsAuthenticated,) 
    serializer_class = CatalogSerializer(many=True)

    def create(self, request, *args, **kwargs):
        start_time = time.time()
        bulk_catalogs = []
        for catalog in request.data:
            serialized_catalog = CatalogSerializer(data=catalog)
            if serialized_catalog.is_valid():
                bulk_catalogs.append(
                    Catalog(
                        code_1c=serialized_catalog.data.get('code_1c'),
                        name=serialized_catalog.data.get('name'),
                        slug=slugify(serialized_catalog.data.get('name')),
                    )
                )
                #return Response({'response': 'Catalog update set in queue!'}, status=status.HTTP_200_OK)
            else:
                return Response({'response catalog update': f'Error!: {serialized_catalog.errors}'}, status=status.HTTP_200_OK)
        catalogs_obj = Catalog.objects.bulk_create(
            bulk_catalogs,
            update_conflicts=True,
            update_fields=['name', 'slug'],
            unique_fields=['code_1c']
        )
        print(f'Catalogs update at {time.time()-start_time} seconds')
        return Response({'response': 'OK!'}, status=status.HTTP_200_OK)


class InitialUploadProducts(viewsets.ModelViewSet):
    """
        *** Upload products ***
        POST: /api/v1/initial_upload_products/
        HEADER: 'Authorization': f'Bearer {token}'
        JSON: {data: [products]}
    """

    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = ProductInitialSerializer(many=True)

    def create(self, request, *args, **kwargs):
        start_time = time.time()
        bulk_products = []
        for product in request.data:
            serialized_product = ProductInitialSerializer(data=product)
            if serialized_product.is_valid():
                catalog = Catalog.objects.get(code_1c=product.get('catalog'))
                bulk_products.append(
                    Product(
                        code_1c=serialized_product.data.get('code_1c'),
                        #name=serialized_product.data.get('name'),
                        price=serialized_product.data.get('price'),
                        quantity=serialized_product.data.get('quantity'),
                        catalog=catalog,
                        description='Нет описания',
                        slug=slugify(serialized_product.data.get('name')),
                    )
                )

            else:
                #logger.error(f'Product serialized error! wit error={serialized_product_in_catalog.errors}')
                return Response({'response products update': f'Error!: {serialized_product.errors}'}, status=status.HTTP_200_OK)
        product_objs = Product.objects.bulk_create(
            bulk_products,
            update_conflicts=True,
            update_fields=['name', 'slug', 'price', 'quantity', 'catalog'],
            unique_fields=['code_1c']
        )
        print(f'Products update at {time.time() - start_time} seconds')
        return Response({'response': 'OK!'}, status=status.HTTP_200_OK)


class CartsViewSet(viewsets.ModelViewSet):

    """
        *** Get all carts ***
        GET: /api/v1/carts/
        HEADER: 'Authorization': f'Bearer {token}'
    """    

    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all().prefetch_related('products')
    serializer_class = CartSerializer

    def update(self, request, pk=None):
        cart = Cart.objects.get(pk=pk)
        ProductInCart.objects.filter(cart=cart).delete()
        products_serializsed = ProductInCartSerializer(data=request.data.get('products'), many=True)
        if products_serializsed.is_valid():
            products_serializsed.save()
            return Response('ok', status=status.HTTP_200_OK)
        else: 
            return Response(products_serializsed.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CustomersViewSet(viewsets.ModelViewSet):

    '''
        -   Create Customer
            POST: http://127.0.0.1:8000/api/v1/customers/
            JSON: {customer}

        -   Get all customers
            GET: http://127.0.0.1:8000/api/v1/customers/
            HEADER: 'Authorization': f'Bearer {token}'

        -   Get customers by pk
            GET: http://127.0.0.1:8000/api/v1/customers/{pk}/
            HEADER: 'Authorization': f'Bearer {token}'

        -   Get customers by phone number
            GET: http://127.0.0.1:8000/api/v1/customers/get_customer_by_phone/
            HEADER: 'Authorization': f'Bearer {token}'
            json: {'phone_number': phone_number a.k. +79999999999}

        -   Activate Customer by token
            POST: http://127.0.0.1:8000/api/v1/customers/user_activation/?q={token}

        -   Update customer information
            POST: http://127.0.0.1:8000/api/v1/customers/customer_update/
            HEADER: 'Authorization': f'Bearer {token}'
            json: {'phone_number': phone number, 'firstName': first name, 'lastName': last name, 'email': email, 'address': address}

        -   Upload customer avatar
            POST: http://127.0.0.1:8000/api/v1/customers/update_avatar/
            HEADER: {'Authorization': `Bearer ${token}`, 'Content-Type': 'multipart/form-data'}
            data: formData

    '''
    permission_classes = []
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
                
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            upended_data = CustomerSerializer(customer, context={'request': request}).data
            refresh_token = RefreshToken.for_user(customer)
            upended_data['access'] = str(refresh_token.access_token)
            upended_data['refresh'] = str(refresh_token)

            return Response(upended_data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'User with this pk does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def get_customer_by_phone(self, request, pk=None):
        try:
            customer = Customer.objects.get(phone_number=request.data.get('phone_number'))
            return Response(CustomerSerializer(customer, context={'request': request}).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'User with this phone number does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def user_activation(self, request, pk=None):
        token = self.request.query_params.get('q')
        if not token:
            return Response({'error': 'At request have no token!'}, status=status.HTTP_400_BAD_REQUEST)
        
        signer = Signer()
        try:
            unsign_object = signer.unsign_object(token[:-1]) # Отбрасываем последний символ так как там слэш
            user = Customer.objects.get(pk=unsign_object['user_id'])
            user.is_active = True
            user.save()

            refresh_token = RefreshToken.for_user(user)
            data = {
                'access': str(refresh_token.access_token),
                'refresh': str(refresh_token)
            }

            return Response({'data': data}, status=status.HTTP_200_OK)

        except signing.BadSignature:
            return Response({'error': 'Непраильный токен активации'}, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response({'error': 'Такого пользователя нет'}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=False, methods=['post'])
    def customer_update(self, request):
        try:
            customer = request.user
            customer.first_name = request.data.get('firstName')
            customer.last_name = request.data.get('lastName')
            customer.address = request.data.get('address')
            customer.save()
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'User error'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=False, methods=['post'], name='update_avatar')
    def update_avatar(self, request):
        try:
            customer = request.user
            customer.avatar = request.FILES.get('file')
            customer.save()
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)


    def get_permissions(self):
        if self.action == 'create' or self.action == 'user_activation':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class GetTokenViewSet(viewsets.ModelViewSet):

    """
        - User login
        POST: /api/v1/token/
        HEADER: {'Content-Type': 'application/json;charset=utf-8'}
        DATA: {'phone_number': phone number, 'password': password}

    """

    permission_classes = [AllowAny]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(methods=['post'], detail=False)
    def login(self, request):
        #user = authenticate(phone_number=request.data.get('phone_number'), password=request.data.get('password'))
        user = None
        try:
            user = Customer.objects.get(phone_number=request.data.get('phone_number'))
        except ObjectDoesNotExist:
            return Response({'error': 'wrong tel or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': 'User is not active! Activate account from email.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if user is not None and check_password(request.data.get('password'), user.password):
            refresh = RefreshToken.for_user(user)

            return Response({'user_id': user.pk, 'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'wrong tel or password'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['post'], detail=False)
    def refresh(self, request):
        pass


class OrderViewSet(viewsets.ModelViewSet):
    '''
        -   Get all orders
            GET: http://127.0.0.1:8000/api/v1/order/
            headers: {'Authorization': Bearer token},

        -   Get order by id
            GET: http://127.0.0.1:8000/api/v1/{pk}/order/
            headers: {'Authorization': Bearer token},

        -   Get user orders
            GET: http://127.0.0.1:8000/api/v1/order/get_orders/
            headers: {'Authorization': Bearer token},

        -   Create new order
            POST: http://127.0.0.1:8000/api/v1/order/
            headers: {'Authorization': Bearer token},
            JSON: {'order_products': [order_products]}

        -   Get order with status ready
            GET: /api/v1/order/get_ready_orders/
            headers: {'Authorization': Bearer token},

        -   Get order with status processing
            GET: /api/v1/order/get_proccessing_orders/
            headers: {'Authorization': Bearer token},

        -   Get order with status 'выдан'
            GET: /api/v1/order/get_history_orders/
            headers: {'Authorization': Bearer token},        
    '''

    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order = None
        try:
            user = request.user
            for item in request.data.get('order_products'): 
                order = Order.objects.create(customer=user)              
                item['order']=order.pk
                item_serialized = CreateOrderProductSerializer(data=item)
                if item_serialized.is_valid():
                    item_serialized.save()
                else:
                    return Response({'error': item_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
                    
            return Response({'response': 'ok'}, status=status.HTTP_200_OK)
            
        except KeyError:
            if order is not None:
                order.delete()
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            if order is not None:
                order.delete()
            return Response({'error': 'Bad request! User does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

            
    def retrieve(self, request, pk):
        order = Order.objects.get(pk=pk)
        return Response(OrderSerializer(order,  context={'request': request}).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], name='user_orders')
    def get_orders(self, request):
        try:
            user = request.user
            # Выдаем все заказы
            orders = Order.objects.filter(customer=user).prefetch_related('order_products').order_by('-order_create')
            return Response(OrderSerializer(orders, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This user does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], name='user_ready_orders')
    def get_ready_orders(self, request):
        try:
            user = request.user
            # Выдаем заказы с статуса 'Готов к выдаче'
            orders = Order.objects.filter(customer=user).prefetch_related('order_products').filter(order_status__status='Готов к выдаче').order_by('-order_create')
            return Response(OrderSerializer(orders, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This user does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)    
        
    @action(detail=False, methods=['get'], name='user_proccessing_orders')
    def get_proccessing_orders(self, request):
        try:
            user = request.user
            # Выдаем заказы с статусом 'Принят, В обработке, в сборке'
            orders = Order.objects.filter(customer=user).prefetch_related('order_products').filter(order_status__status__in=['Принят', 'В обработке', 'В сборке']).order_by('-order_create')
            return Response(OrderSerializer(orders, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This user does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'], name='user_history_orders')
    def get_history_orders(self, request):
        try:
            user = request.user
            # Выдаем заказы с статусом 'Принят, В обработке, в сборке'
            orders = Order.objects.filter(customer=user).prefetch_related('order_products').filter(order_status__status__in=['Выдан']).order_by('-order_create')
            return Response(OrderSerializer(orders, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This user does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)         
        

class Likes(viewsets.ViewSet):

    """
        -   Add like/dislike
            POST: http://127.0.0.1:8000/api/v1/like/
            headers: {'Authorization': Bearer token},
            data: {'product_id': id, 'operation': 'like/dislike'}

        -   Get liked products
            POST: /api/v1/like/get_sliced_liked_products/
            headers: {'Authorization': Bearer token},
            data: [likedProducts] (list of user liked id products)
    """

    permission_classes = (IsAuthenticated,)

    def create(self, request):
        try:
            customer = request.user
            if not customer.is_active:
                return Response({'error': 'This user is not active!'}, status=status.HTTP_401_UNAUTHORIZED)
            
            product = Product.objects.get(pk=request.data.get('product_id'))

            if request.data.get('operation') == 'like':
                customer.likes.add(product)
            else:
                customer.likes.remove(product)

            customer.save()
            return Response({'response': 'Liked!'}, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'This user is not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        
        except KeyError:
            return Response({'error': 'Bad request!'}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'], name='liked_sliced_products')
    def get_sliced_liked_products(self, request):
        liked_products = Product.objects.filter(pk__in=request.data)
        return Response(ProductSerializer(liked_products, context={'request': request}, many=True).data, status=status.HTTP_200_OK)
    

    def get_permissions(self):
        if self.action in ['update', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
    

class FeedbackViewSet(viewsets.ModelViewSet):
    
    """
        *** Get all published Feedbacks ***
        - GET: /api/v1/feedbacks/
        - Premissions: AllowAny

        *** Send feedback ***
        - POST: /api/v1/feedbacks/
        - Permissions: IsAuthenticated

    """

    queryset = Feedback.objects.filter(is_show=True)
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.action in ['update', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
    

class ProductQuestionViewSet(viewsets.ModelViewSet):

    '''
        *** Get all questions ***
        - GET: '/api/v1/questions/'
        - Permissions: AllowAny

        *** Create question ***
        - POST: '/api/v1/questions/'
        - Permissions: IsAuthenticated
        - Data: {'product': id, 'customer': id, 'text': text}
    '''

    queryset = ProductQuestion.objects.all()
    serializer_class = ProductQuestionSerializer

    def get_permissions(self):
        if self.action in ['update', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
    

class CatalogViewSet(viewsets.ModelViewSet):

    '''
        *** Get all catalogs ***
        - GET '/api/v1/calalogs'
        - Premission: AllowAny
    '''

    queryset = Catalog.objects.filter(is_active=True)
    serializer_class = CatalogSerializer

    def get_permissions(self):
        if self.action in ['update', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]