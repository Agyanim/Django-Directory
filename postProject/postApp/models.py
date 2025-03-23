from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices = [('FICTION' ,'Fiction'), ('BIOGRAPHY','Biography' ), ('ROMANS','Romans'), ('POETRY','Poetry'),], default='FICTION')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.title
    
    class Meta(): 
       ordering = ['-createdAt' ]
    