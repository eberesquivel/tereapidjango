from django.shortcuts import render
from rest_framework import viewsets 
from .models import Cerveza
from .serializers import CervezaSerializer
# Create your views here.

class ChelaViewSet(viewsets.ModelViewSet):
    serializer_class = CervezaSerializer
    queryset = Cerveza.objects.all()