from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(default='Defult Title')
    blog_text = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.blog_text[:30]}'