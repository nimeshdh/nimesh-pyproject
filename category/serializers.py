# category/serializers.py
from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }