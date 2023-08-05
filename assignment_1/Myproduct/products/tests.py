from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product

class ProductAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': 59.93,
            'quantity': 10
        }
        response = self.client.post('http://127.0.0.1:8000/product/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        response = self.client.get('http://127.0.0.1:8000/product/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_product(self):
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, quantity=10)
        response = self.client.get(f'http://127.0.0.1:8000/product/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, quantity=10)
        data = {
            'name': 'Updated Product',
            'description': 'This is an updated test product.',
            'price': 2.99,
            'quantity': 5
        }
        response = self.client.put(f'http://127.0.0.1:8000/product/products/{product.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, quantity=10)
        response = self.client.delete(f'http://127.0.0.1:8000/product/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_add_product_custom_action(self):
        data = {
            'name': 'Custom Action Product',
            'description': 'This is a custom action test product.',
            'price': 39.99,
            'quantity': 8
        }
        response = self.client.post('http://127.0.0.1:8000/product/products/add-product/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product_custom_action(self):
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, quantity=10)
        data = {
            'name': 'Updated Custom Action Product',
            'description': 'This is an updated custom action test product.',
            'price': 390.99,
            'quantity': 3
        }
        response = self.client.put(f'http://127.0.0.1:8000/product/products/{product.id}/update-product/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product_custom_action(self):
        product = Product.objects.create(name='Test Product', description='This is a test product.', price=19.99, quantity=10)
        response = self.client.delete(f'http://127.0.0.1:8000/product/products/{product.id}/delete-product/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

