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
from api.serializers import CartSerializer, CatalogSerializer, CustomerSerializer, ProductInitialSerializer, ProductListSerializer, ProductSerializer
from main.models import Cart, Catalog, Customer, CustomerLoginFail, Product
from main.email_functional import send_mail
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from rest_framework.views import APIView


class ProductViewSet(viewsets.ModelViewSet):
    """
        *** Get Products ***
        /api/v1/products/ - get all products
        /api/v1/products/{pk}/ - get product by pk
    """
    permission_classes = []
    queryset = Product.objects.filter(quantity__gt=0).order_by('?')
    serializer_class = ProductListSerializer
    #@method_decorator(cache_page(60 * 60 * 2))
    #@method_decorator(vary_on_cookie)

    def retrieve(self, request, pk):
        product = Product.objects.get(pk=pk)
        return Response(ProductSerializer(product,  context={'request': request}).data, status=status.HTTP_200_OK)


class InitialUploadCatalog(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CatalogSerializer(many=True)

    def create(self, request, *args, **kwargs):
        for catalog in request.data:
            serialized_catalog = CatalogSerializer(data=catalog)
            if serialized_catalog.is_valid():
                obj, created = Catalog.objects.update_or_create(
                    code_1c=serialized_catalog.data.get('code_1c'),
                    defaults={
                        'name': serialized_catalog.data.get('name')
                    }
                )
                #return Response({'response': 'Catalog update set in queue!'}, status=status.HTTP_200_OK)
            else:
                return Response({'response': f'Error!: {serialized_catalog.error_messages}'}, status=status.HTTP_200_OK)
            
        return Response({'response': 'OK!'}, status=status.HTTP_200_OK)


class InitialUploadProducts(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ProductInitialSerializer(many=True)

    def create(self, request, *args, **kwargs):
        for product in request.data:
            print(product)
            serialized_product = ProductInitialSerializer(data=product)
            print(serialized_product)
            if serialized_product.is_valid():
                print(product.get('catalog'))
                catalog = Catalog.objects.get(code_1c=product.get('catalog'))
                print(catalog)
                obj, created = Product.objects.update_or_create(
                    code_1c=serialized_product.data.get('code_1c'),
                    defaults={
                        'name': serialized_product.data.get('name'),
                        'price': serialized_product.data.get('price'),
                        'quantity': serialized_product.data.get('quantity'),
                        'catalog': catalog,
                        'description': 'Нет описания',
                    }
                )
                #products.append(obj)
                #return Response({'response': 'Products update set in queue!'}, status=status.HTTP_200_OK)

            else:
                #logger.error(f'Product serialized error! wit error={serialized_product_in_catalog.errors}')
                print(serialized_product.errors)
                return Response({'response': f'Error!: {serialized_product.error_messages}'}, status=status.HTTP_200_OK)
        
        return Response({'response': 'OK!'}, status=status.HTTP_200_OK)
        

class CartsViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CustomersViewSet(viewsets.ModelViewSet):

    '''
        -   Create Customer
            POST: http://127.0.0.1:8000/api/v1/customers/
            json: {customer}

        -   Get all customers
            GET: http://127.0.0.1:8000/api/v1/customers/

        -   Get customers by pk
            GET: http://127.0.0.1:8000/api/v1/customers/{pk}/

        -   Get customers by phone number
            GET: http://127.0.0.1:8000/api/v1/customers/get_customer_by_phone/
            json: {'phone_number': phone_number a.k. +79999999999}

        -   Activate Customer by token
            POST: http://127.0.0.1:8000/api/v1/customers/user_activation/?q={token}

    '''
    permission_classes = []
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serialized_customer = CustomerSerializer(data=request.data)
        if serialized_customer.is_valid():
            #user = serialized_customer.save()
            user = Customer.objects.create_user(
                password=serialized_customer.data.get('password'),
                email=serialized_customer.data.get('email'),
                first_name=serialized_customer.data.get('first_name', 'None'),
                last_name=serialized_customer.data.get('last_name', 'None'),
                is_read_pd=serialized_customer.data.get('is_read_pd', False),
                phone_number=serialized_customer.data.get('phone_number'),
                address=serialized_customer.data.get('address', 'none'),
                is_active=False
                )
            user.save()
            token = self.get_tokens_for_user(user)

            result = send_mail(request, user)
            if result.get('response') != 'ok':
                return Response({'status': 'BAD', 'error': result}, status=status.HTTP_400_BAD_REQUEST)    
            return Response({'status': 'OK', 'tokens': token}, status=status.HTTP_200_OK)
            
        else:
            print(serialized_customer.error_messages)
            print(serialized_customer.errors)
            return Response({'response': {'error': serialized_customer.errors}}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'User with this pk does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def get_customer_by_phone(self, request, pk=None):
        try:
            customer = Customer.objects.get(phone_number=request.data.get('phone_number'))
            return Response(CustomerSerializer(customer).data, status=status.HTTP_200_OK)
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


    def get_permissions(self):
        if self.action == 'create' or 'user_activation':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        

 
class TokenView(viewsets.ViewSet):

    LOGIN_FAIL_DELTA = timezone.timedelta(hours=1)

    @action(methods=['post'], detail=False)
    def get(self, request):
        try:
            user = authenticate(request, username=request.data.get('phone_number'), password=request.data.get('password'))
            
            if user is not None:
                # Юзер такой есть
                if not user.ban_status:
                    # юзер не забанен
                    refresh = RefreshToken.for_user(user)
                    
                    # юзер удачно зашел, обнуляем счетчик неудачных входов
                    user.login_fail_counter = 0
                    user.save()
                
                    return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'You are banned!'}, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                # Такого юзера нет или неправильный пароль
                try:
                    find_user = Customer.objects.get(phone_number=request.data.get('phone_number'))
                    # Такой пользователь есть, значит ошиблись с паролем.

                    if find_user.login_fail_counter > 4:
                        # это пятая и более попытка. Баним.
                        find_user.ban_status = True
                        find_user.login_fail_counter += 1
                        find_user.save()
                        return Response({'error': 'To much try! You banned!'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        # Попытки еще есть
                        find_user.login_fail_counter += 1
                        find_user.save()
                        return Response({'error': 'Wrong password!'}, status=status.HTTP_400_BAD_REQUEST)

                except ObjectDoesNotExist:
                    return Response({'error': 'User with this tel number is absent'}, status=status.HTTP_400_BAD_REQUEST)

                '''
                login_fail = CustomerLoginFail.objects.filter(customer=user)
                if not login_fail:
                    # неудачных входов не было
                    obj = CustomerLoginFail.objects.create(
                        customer=user,
                    )
                    obj.save()
                    user.login_fail_counter = 1
                    user.save()
                    return Response({'error': 'tel or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
                
                else:
                    # Очередной неудачный вход
                    if user.login_fail_counter > 4:
                        # Баним пользователя
                        user.ban_status = True
                        user.login_fail_counter += 1
                        user.save()
                        return Response({'error': 'To big incorrect try enter password! You are banned!'}, status=status.HTTP_400_BAD_REQUEST)
                    
                    else:
                        # Сообщаем о неверном пароле и увеличиваем неудачных входов на 1
                        user.login_fail_counter += 1
                        user.save()
                        return Response({'error': 'tel or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
                '''    
                return Response({'error': 'login or password is icorrect!'}, status=status.HTTP_400_BAD_REQUEST)
            
        except PermissionDenied:
            return Response({'error': 'This user does not exist'}, status=status.HTTP_400_BAD_REQUEST)