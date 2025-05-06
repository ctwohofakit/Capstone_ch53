from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Account(AbstractUser):
    email=models.EmailField("email address", unique=True, blank=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[] 

    #auto assign username
    def save(self, *args, **kwargs):
        if not self.username:
            self.username=self.email
        super().save(*args,**kwargs)

    def __str__(self):
        return self.email



class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address_line_1=models.CharField(max_length=150, blank=True)
    address_line_2=models.CharField(max_length=150, blank=True)
    city=models.CharField(max_length=30, blank=True)
    state=models.CharField(max_length=20, blank=True)
    country=models.CharField(max_length=50, blank=True)
    profile_picture=models.ImageField(upload_to="images/users", blank=True, null=True)
    zip_code=models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user} profile"

