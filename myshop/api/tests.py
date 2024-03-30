from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from main.models import Product



class AccountTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_product(self):
        url = reverse('products')
        data = {'name': 'DabApps'}
        response = self.client.get(url, params=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(Product.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')

    def test_product_retrieve(self):
        url = reverse('products')
        data = {'pk': 1}
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(Product.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')