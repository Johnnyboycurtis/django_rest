from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


def home(request):
    return render(request, template_name='basic/home.html')

class FirstView(viewsets.ModelViewSet):
    queryset = models.First.objects.all()
    serializer_class = serializers.FirstSerializer


class SecondView(viewsets.ModelViewSet):
    queryset = models.Second.objects.all()
    serializer_class = serializers.SecondSerializer



