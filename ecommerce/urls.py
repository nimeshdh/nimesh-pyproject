from django.urls import path
from ecommerce import views

# Create your views here.
urlpatterns = [
    path('home/', views.home)
]
