from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentListCreateAPIView

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('payment-list/', PaymentListCreateAPIView.as_view(),
         name='payment-list-create'),
]
