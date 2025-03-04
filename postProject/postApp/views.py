from django.shortcuts import render
from .form import UserForm

# Create your views here.


def index(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'postApp/login.html')

def createUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context= {'form': form}
    return render(request, 'postApp/create-user.html', context)
