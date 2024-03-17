from django.db import models
from django.conf import settings
from django.forms import JSONField
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    USER_TYPE_CHOICES = (
        ("creator", "Creator"),
        ("advertiser", "Advertiser"),
        ("association", "Association"),
    )
    user_type = models.CharField(max_length=14, choices=USER_TYPE_CHOICES)
    
    def is_creator(self):
        return self.user_type == "creator"

    def is_advertiser(self):
        return self.user_type == "advertiser"

    def is_association(self):
        return self.user_type == "association"

class CustomUserProfile(models.Model):

    name = models.CharField(max_length=255, unique=True, default="SOME STRING")
    social_links = models.JSONField(default=dict)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    main_description = models.TextField(
        verbose_name="Description",
        help_text="Enter a description for your model",
        null=True,
        blank=True,
    )
    partners = models.JSONField(default=dict)
    campaigns = models.JSONField(default=dict)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True, default='static/images/default_banner.jpg')
