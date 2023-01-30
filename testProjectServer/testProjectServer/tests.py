import json
import os
from pprint import pprint

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from api.models import Client, ClientProfile
from django.test import TestCase
from rest_framework.test import APIClient


class TestProjectTestCase(TestCase):
    def login(self):
        self.credentials = {
            'username': 'admin',
            'password': 'admin',
        }
        self.client = APIClient()
        login_data = self.client.post('/api/token/', json.dumps(self.credentials),
                                      content_type='application/json')
        token = login_data.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def setUp(self):
        self.login()

    def test_test(self):
        self.assertEqual(1, 1)

    def test_client_create(self):
        data = {
            'first_name': 'Alex',
            'last_name': 'Ivanov',
            'gender': 'male',
            'photo_url': 'photo'
        }
        response = self.client.post('/api/client', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_client_update(self):
        data = {
            'first_name': 'Alex',
            'last_name': 'Ivanov',
            'gender': 'male',
            'photo_url': 'photo'
        }
        response = self.client.post('/api/client', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        id = json.loads(response.content)['id']

        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'gender': 'male',
            'photo_url': 'new photo'
        }
        response = self.client.put(f'/api/client/{id}', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        item = json.loads(response.content)
        self.assertEqual(item['photoUrl'], 'new photo')

    def test_client_delete(self):
        data = {
            'first_name': 'Alex',
            'last_name': 'Ivanov',
            'gender': 'male',
            'photo_url': 'photo'
        }
        response = self.client.post('/api/client', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        id = json.loads(response.content)['id']

        response = self.client.delete(f'/api/client/{id}', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(list(Client.objects.all()), list())
        self.assertEqual(list(ClientProfile.objects.all()), list())

    def test_client_get(self):
        data = {
            'first_name': 'Alex',
            'last_name': 'Ivanov',
            'gender': 'male',
            'photo_url': 'photo'
        }
        response = self.client.post('/api/client', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'/api/client/get-all-clients', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_weather(self):
        data = {
            'date': 'date',
            'city': 'London'
        }
        response = self.client.post('/api/weather',data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        pprint(json.loads(response.content))

    def test_get_disk_usage(self):
        response = self.client.get('/api/get-disk-usage', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        pprint(json.loads(response.content))
