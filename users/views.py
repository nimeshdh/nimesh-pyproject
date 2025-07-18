from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import response
from users.models import Users
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializers


def create(request):
    return HttpResponse("This is a create page")


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
