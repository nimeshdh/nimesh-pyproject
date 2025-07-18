from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True)  # Optional: shows username

    class Meta:
        model = Order
        fields = ['id', 'order_name', 'user', 'placed_at', 'payment_status']
