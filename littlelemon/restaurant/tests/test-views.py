from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(Name='Pizza', Price=10.99, Inventory=100)
        self.menu2 = Menu.objects.create(Name='Salad', Price=5.99, Inventory=100)
        self.menu3 = Menu.objects.create(Name='Ice Cream', Price=3.99, Inventory=100)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
