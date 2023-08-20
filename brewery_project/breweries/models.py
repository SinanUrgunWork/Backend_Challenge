from django.contrib.auth.models import User
from django.db import models
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Brewery(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    brewery_type = models.CharField(max_length=50, blank=True, null=True)
    address_1 = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)

    users_interacted = models.ManyToManyField(UserProfile, related_name='interacted_breweries')

    def __str__(self):
        return self.name
