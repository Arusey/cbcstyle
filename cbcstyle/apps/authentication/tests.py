from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_user_url = reverse('user-create')
        self.login_user_url = reverse('user-login')
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
        }
    
    def test_create_user(self):
        response = self.client.post(self.create_user_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

        user = User.objects.get(email=self.user_data['email'])
        self.assertEqual(user.email, self.user_data['email'])
    
    def test_login_user(self):
        user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            first_name='John',
            last_name='Doe'
        )
        
        response = self.client.post(self.login_user_url, {'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
    
    def test_invalid_credentials(self):
        response = self.client.post(self.login_user_url, {'email': 'test@example.com', 'password': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('token', response.data)
