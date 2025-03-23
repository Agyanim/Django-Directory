from django.shortcuts import render, redirect
from .form import UserForm,CreatePostForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Post



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
        email=request.POST['email']
        username=request.POST['username']
        is_user = None       
        if email == "":
            messages.warning(request,"Email field cannot be empty")
            return redirect("signup")
        is_user = User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()
        if is_user:
            messages.warning(request,'Username or Email already taken')
            return redirect("signup")
        form = UserForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')      
        return redirect("signup")
    return render(request, 'postApp/signup.html', context)

def logout(request):
    auth.logout(request)
    return redirect("index")

def posts(request):
    userPosts = Post.objects.all()
    if userPosts:
       return render(request,'postApp/posts.html',{"posts":userPosts})
    return render(request,'postApp/posts.html',{"notes":"No post available now"})

def editPost(request,id):
    
    return render(request,'postApp/edit-post.html',{"id":id})

def createPost(request):
    form = CreatePostForm
    context ={"form":form}
    return render(request,'postApp/create-post.html',context)
    