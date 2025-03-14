from django.shortcuts import render, redirect
from .form import UserForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, 'postApp/home.html')


def about(request):
    return render(request, 'postApp/about.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if username == "":
            messages.info(request,'Username field cannot be empty')
            return redirect('login')
        elif password == '':
            messages.info(request,'Password field cannot be empty')
            return redirect('login')
        else:  
            user=auth.authenticate(request,username=username, password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('posts')
            else:
                messages.info(request, 'Username or password incorrect') 
    return render(request, 'postApp/login.html')

def signup(request):
    form = UserForm()
    context= {'form': form}
    
    if request.method == 'POST':
        
        # username=request['username']
        # email=request['email']
        # password=request['password']
        # is_user = None
        
        # if username=="":
        #     return messages.warning(request,"Username cannot be empty")
        # elif email == "":
        #     return messages.warning(request,"Email cannot be empty")
        # elif password == "" or len(password) > 6:
        #     return messages.warning(request,'Password cannot be empty or less than 6 characters')
        # else:
        #     is_user=User.objects.filter(email=email).exists()
        #     print(is_user)
                
            
         
        form = UserForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')      
        else:
            return render(request, 'postApp/signup.html', context)
    
    return render(request, 'postApp/signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect("index")

def posts(request):
    return render(request,'postApp/posts.html')
