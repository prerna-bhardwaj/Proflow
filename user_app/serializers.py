from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'