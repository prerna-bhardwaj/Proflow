from rest_framework import serializers
from .models import *


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommunitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectDescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectDescription
        fields = '__all__'


class ProjectImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'

