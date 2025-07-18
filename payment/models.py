

# Create your models here.
from django.db import models
from users.models import Users  # Adjust according to your user model path


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('COD', 'Cash on Delivery'),
        ('CARD', 'Card'),
        ('ESewa', 'ESewa'),
        ('Khalti', 'Khalti'),
    ]

    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, default="Pending")  # Optional field

    def __str__(self):
        return f"{self.user.full_name} - {self.amount} ({self.method})"
