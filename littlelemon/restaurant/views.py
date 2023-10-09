from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.

def index(request):
    return render(request, 'restaurant/index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer