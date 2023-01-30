from django.db import models


class ClientProfile(models.Model):
    photo_url = models.TextField(null=True, blank=True, default=None)


class Client(models.Model):
    profile = models.OneToOneField(ClientProfile, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField(null=True, default=None)
    gender = models.CharField(max_length=10, null=True, default=None)
