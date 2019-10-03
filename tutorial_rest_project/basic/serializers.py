from . import models
from rest_framework import serializers

class FirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.First
        fields = ('id', 'name', 'form_type', 'comments')


class SecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Second
        fields = ('id', 'user', 'name', 'form_type', 'comments')

