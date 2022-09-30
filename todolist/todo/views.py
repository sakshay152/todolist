from django.shortcuts import render
from rest_framework import generics
from todo.models import Book
from todo.serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book
    serializer_class=BookSerializer
