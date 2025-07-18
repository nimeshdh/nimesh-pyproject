from .views import UserViewSet
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    
    path('create/', views.create, name="create-page"),
]
router = DefaultRouter()
router.register("user", views.UserViewSet)
urlpatterns += router.urls

