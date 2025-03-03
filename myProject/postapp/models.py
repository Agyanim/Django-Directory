from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField(max_length=255),
    description = models.TextField(null=True, blank=True),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    