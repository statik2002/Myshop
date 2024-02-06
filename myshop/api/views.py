from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import CatalogSerializer, ProductInitialSerializer, ProductListSerializer, ProductSerializer
from main.models import Catalog, Product


class ProductViewSet(viewsets.ModelViewSet):
    """
        *** Get Products ***
        /api/v1/products/ - get all products
        /api/v1/products/{pk}/get_product/ - get product by pk
    """
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.filter(quantity__gt=0)
    serializer_class = ProductListSerializer

    @action(methods=['get'], detail=True)
    def get_product(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)


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
        