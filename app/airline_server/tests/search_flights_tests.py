from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Flight, Place, Route
from ..serializers import SearchFlightOutputSerializer


class SearchFlightsTestCase(APITestCase):
    def setUp(self):
        self.client = Client()
        Place.objects.create(id='1bc2a30a-4557-4a41-9513-c1b517d48c89', country='US',
                             airport_city='New York', airport_name='New Airport')
        Place.objects.create(id='32f617f8-ed5b-469f-b40a-3c9f3085dade', country='US',
                             airport_city='California', airport_name='California Main Airport')

        Route.objects.create(id='6c28e6df-63d6-4d33-a743-5ae0cded80c3',
                             start_point=Place.objects.get(id='1bc2a30a-4557-4a41-9513-c1b517d48c89'),
                             end_point=Place.objects.get(id='32f617f8-ed5b-469f-b40a-3c9f3085dade'))
        Route.objects.create(id='740cb121-e1b7-416a-a5e3-97ec2d32ef81',
                             start_point=Place.objects.get(id='32f617f8-ed5b-469f-b40a-3c9f3085dade'),
                             end_point=Place.objects.get(id='1bc2a30a-4557-4a41-9513-c1b517d48c89'))
        Flight.objects.create(id='a3af0a9a-f959-4f3a-9806-4a2820c869ac',
                              route=Route.objects.get(id='6c28e6df-63d6-4d33-a743-5ae0cded80c3'),
                              date_of_departure=timezone.now(), ticket_price=150,
                              number_of_seats=15, number_of_free_spaces=3
                              )
        Flight.objects.create(id='f4dd25da-35c2-4f60-b6ac-fd7f2db96698',
                              route=Route.objects.get(id='740cb121-e1b7-416a-a5e3-97ec2d32ef81'),
                              date_of_departure=timezone.now().replace(day=timezone.now().day + 1),
                              ticket_price=120, number_of_seats=200, number_of_free_spaces=0
                              )

    def test_get_all_flights(self):
        response = self.client.get('/api/search/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_get_today_flights(self):
        response = self.client.get('/api/search/?date=' + str(timezone.now().date()) +
                                   '&start_point=&end_point=&space_needed=')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_tomorrow_flights(self):
        response = self.client.get('/api/search/?date=' +
                                   str(timezone.now().replace(day=timezone.now().day + 1).date()) +
                                   '&start_point=&end_point=&space_needed=')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_not_full_flights(self):
        response = self.client.get('/api/search/?date=&start_point=&end_point=&space_needed=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_set_start_point_flights(self):
        response = self.client.get('/api/search/?date=&start_point=32f617f8-ed5b-469f-b40a-3c9f3085dade&end_point=&space_needed=')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_set_end_point_flights(self):
        response = self.client.get('/api/search/?date=&start_point=&end_point=32f617f8-ed5b-469f-b40a-3c9f3085dade&space_needed=')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_set_start_point_no_space_flights(self):
        response = self.client.get('/api/search/?date=&start_point=32f617f8-ed5b-469f-b40a-3c9f3085dade&end_point=&space_needed=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_get_set_end_point_has_free_space_flights(self):
        response = self.client.get('/api/search/?date=&start_point=&end_point=32f617f8-ed5b-469f-b40a-3c9f3085dade&space_needed=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)