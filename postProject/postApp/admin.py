from django.contrib import admin
from .models import Posts
from . import models

# Register your models here.

admin.site.register(models.Posts)