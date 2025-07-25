from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryListCreateAPIView

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListCreateAPIView.as_view(),
         name='category-list-create'),
]
