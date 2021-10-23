from django.contrib.auth.models import User, Group
from .models import Horses
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HorseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horses
        fields = ['id', 'genotype', 'bloodline', 'breed_type', 'horse_type', 'rating']
