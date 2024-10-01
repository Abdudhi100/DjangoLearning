from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# BookView is omitted here, but this is where your views would go

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    
class SingleBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer