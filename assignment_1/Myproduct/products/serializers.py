from importlib.metadata import requires
from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

User=get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, max_digits=12, decimal_places=2)
    quantity = serializers.IntegerField(required=True)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    
    class Meta:
        model = User
        fields = ['email', 'password']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
