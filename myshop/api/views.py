from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.exceptions import ObjectDoesNotExist

from api.serializers import CartSerializer, CatalogSerializer, CustomerSerializer, ProductInitialSerializer, ProductListSerializer, ProductSerializer
from main.models import Cart, Catalog, Customer, Product


class ProductViewSet(viewsets.ModelViewSet):
    """
        *** Get Products ***
        /api/v1/products/ - get all products
        /api/v1/products/{pk}/ - get product by pk
    """
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.filter(quantity__gt=0)
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

    '''

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serialized_customer = CustomerSerializer(data=request.data)
        if serialized_customer.is_valid():
            serialized_customer.save()
            return Response(serialized_customer.data, status=status.HTTP_200_OK)

        else:
            return Response({'response': f'Error!: {serialized_customer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            return Response(CustomerSerializer(customer).data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'User with this pk does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['get'])
    def get_customer_by_phone(self, request, pk=None):
        print(request.data)
        try:
            customer = Customer.objects.get(phone_number=request.data.get('phone_number'))
            return Response(CustomerSerializer(customer).data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'User with this phone number does not exist'}, status=status.HTTP_400_BAD_REQUEST)