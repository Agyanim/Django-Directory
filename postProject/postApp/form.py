from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class CreatePost(ModelForm):
    class Meta:
        model=Post
        fields = ["title","description","category"]
        