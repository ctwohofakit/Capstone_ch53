from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        # If you still have a username column, default it to the email
        extra_fields.setdefault("username", email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff",   True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email, password, **extra_fields)

class Account(AbstractUser):
    email=models.EmailField("email address", unique=True, blank=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[] 

    objects = AccountManager()
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

