from django.db import router
import pytest
from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from main.models import Product
from api.serializers import ProductSerializer
from rest_framework.test import RequestsClient


@pytest.mark.django_db
def test_products_list(client):
    client = RequestsClient()
    base_url = 'http://127.0.0.1:8000/api/v1/'
    
    response = client.get(base_url+'products/1/')

    products = Product.objects.all()
    expected_data = ProductSerializer(products).data

    assert response.status_code == 200
    assert response.json() == expected_data
    
        