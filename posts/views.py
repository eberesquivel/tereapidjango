from django.shortcuts import render
from rest_framework import viewsets 
from .models import Posts
from .serializers import PostSerializer
# Create your views here.

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()