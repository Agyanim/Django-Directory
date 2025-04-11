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
    post_detail = Post.objects.get(id=id)
    if request.method == "POST":
        if post_detail.created_by == request.user:
            form= CreatePostForm(request.POST, instance=post_detail)
            if form.is_valid:
                form.save()
                return redirect('postDetail',id)
        else:
            messages.info(request,"Sorry, you are not authorized to modify this post.")
            return redirect("editPost",id)
    else:
        form=CreatePostForm(instance=post_detail) 
        if post_detail.created_by != request.user:
            messages.info(request,"Sorry, you are not authorized to modify this post.")
            return redirect("postDetail",id)   
        context ={
            "form":form , 
            "post":post_detail,
            }
    return render(request,'postApp/edit-post.html',context)

def deletePost(request,id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if post.created_by == request.user:
            post.delete()
            return redirect('posts')
        else:
            messages.info(request,'Sorry, you are not authorized to delete this post')
            return redirect('postDetail', id)
    return render(request,'postApp/delete-post.html',{"id":id})


def warning(request,id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        if post.created_by == request.user:
            return render(request,'postApp/delete-post.html',{"id":id})
        else:
            messages.info(request,'Sorry, you are not authorized to delete this post')
            return redirect('postDetail',id)
        

    

def postDetails(request,id):
    form = CreatePostForm
   
    post_detail = Post.objects.get(id=id)
    context ={
        "form":form , 
        "post":post_detail,
        }
    
    return render(request,'postApp/post-details.html',context)

def createPost(request):
    print(type(request.user))
    form = CreatePostForm
    if request.method == 'POST':
        post = request.POST
        form = CreatePostForm(post)
        
        if form.is_valid and request.user.is_authenticated:
            submission=form.save(commit=False)
            submission.created_by = request.user
            submission.save()
            return redirect('posts')  
        else:
            messages.info(request,'Sign in to create post')
            return redirect('createPost')
    context ={"form":form}
    return render(request,'postApp/create-post.html',context)
    