from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    title = models.CharField()
    blog_text = models.TextField()
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'