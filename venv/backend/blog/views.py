# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import BlogSerializer      # add this
from .models import Blog                    # add this

class BlogView(viewsets.ModelViewSet):       # add this
  serializer_class = BlogSerializer          # add this
  queryset = Blog.objects.all()              # add this
