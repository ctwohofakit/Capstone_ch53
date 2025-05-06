from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='category_images/',
        default='category_images/default.png',
        blank=True
    )

    def __str__(self):
        return self.name

class Interview(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    wanted_role=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    Question_CHOICES=[('technical','Technical'),('non-technical','Non-Technical')]
    question_type=models.CharField(max_length=50, choices=Question_CHOICES)
    technology=models.CharField(max_length=200)
    created_by=models.DateTimeField(auto_now_add=True)
    is_finished=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.wanted_role}-{self.company_name}-({self.question_type})"
    
class InterviewConvo(models.Model):
    ROLE_CHOICES=[('system','System'),('assistant','Assistant'),('user','User')]
    interview=models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="messages")
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}-{self.content[:30]}..."
    




# class Profile(models.Model):
#     user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio =models.TextField()


#     def __str__(self):
#         return str(self.user)