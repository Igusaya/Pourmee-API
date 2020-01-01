import json
from rest_framework.exceptions import ErrorDetail

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from PourmeeAPI.models import Card


class CardTests(TestCase):

    def test_get(self):
        """
        Nomal test.
        Throw a get request.
        """
        url = '/cards/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post(self):
        """
        Nomal test.
        Assign the maximum value to each item.
        """
        url = '/cards/'
        data = {
                'name': 'test name ########################################',
                'position': 100,
                'color': '#191919',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 1)
        self.assertEqual(Card.objects.get().name, 'test name ########################################')
        self.assertEqual(Card.objects.get().color, '#191919')


    def test_validate_color_max_value(self):
        """
        Boundary value abnomarl test.
        Assign 8 characters to color
        """
        url = '/cards/'
        data = {
                'name': 'test name',
                'position': 100,
                'color': '#1919191',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Card.objects.count(), 0)
        self.assertIn('color', response.data)
        self.assertEqual(response.data['color'][0].code, 'max_length')


    def test_validate_name_max_value(self):
        """
        Boundary value abnomarl test.
        Assign 51 characters to name
        """
        url = '/cards/'
        data = {
                'name': 'test name ########################################1',
                'position': 100,
                'color': '#191919',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Card.objects.count(), 0)
        self.assertIn('name', response.data)
        self.assertEqual(response.data['name'][0].code, 'max_length')

