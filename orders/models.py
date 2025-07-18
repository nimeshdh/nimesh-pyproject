from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed'),
    ]

    order_name = models.CharField(max_length=100)

    # ForeignKey to Django's built-in User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    placed_at = models.DateTimeField(auto_now_add=True)

    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default='P'
    )

    def __str__(self):
        return f"{self.order_name} ({self.get_payment_status_display()})"
