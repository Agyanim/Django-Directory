from django.shortcuts import render, redirect
from .form import UserForm

# Create your views here.


def index(request):
    return render(request, 'postApp/home.html')


def about(request):
    return render(request, 'postApp/about.html')

def login(request):
    if request.method == 'POST':
        # data=request.POST
        print(request.POST)
    return render(request, 'postApp/login.html')

def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')      
        else:
            return render(request, 'postApp/signup.html', {'form': form})
    context= {'form': form}
    return render(request, 'postApp/signup.html', context)
