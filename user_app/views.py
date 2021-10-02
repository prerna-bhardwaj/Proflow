from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from user_app.serializers import *
from .models import *

class NotificationsList(generics.ListAPIView):

    # def get_queryset(self):
    #     userObject = User.objects.get(pk=id)
    #     return Notifications.objects.filter(user=)

    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializers

    lookup_field = 'user'

class CartList(generics.ListAPIView):
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user.pk)

    serializer_class = CartSerializers

