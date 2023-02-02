import datetime
from dataclasses import dataclass

from rest_framework import serializers

from api.models import Client, ClientProfile


class ClientProfileSerializer(serializers.Serializer):
    photo_url = serializers.CharField(default=None)

    def create(self, validated_data):
        return ClientProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        return instance


class ClientSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField(default=None)
    gender = serializers.CharField(default=None)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)

        return instance


class ClientItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField(default=None)
    gender = serializers.CharField(default=None)
    photo_url = serializers.CharField(default=None)


@dataclass
class ClientItem(object):

    id: int
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    gender: str
    photo_url: str
