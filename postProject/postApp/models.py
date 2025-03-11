from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices = [('FICTION' ,'Fiction'), ('BIOGRAPHY','Biography' ), ('ROMANS','Romans'), ('POETRY','Poetry'),], default='FICTION')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta(): 
       ordering = ['-createdAt' ]
    