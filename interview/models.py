from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Interview(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    wanted_role=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    Question_CHOICES=[('technical','Technical'),('non-technical','Non-Technical')]
    question_type=models.CharField(max_length=50, choices=Question_CHOICES)
    technology=models.CharField(max_length=200)
    created_by=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wanted_role}-{self.comapny_name}-({self.question_type})"
    
class InterviewConvo(models.Model):
    ROLE_CHOICES=[('system','System'),('assistant','Assistant'),('user','User')]
    interview=models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="messages")
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}-{self.content[:30]}..."
    

    