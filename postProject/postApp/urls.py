from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('post/create/',views.createPost, name='createPost'),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:id>', views.postDetails, name='postDetail'),
    path('post/edit/<str:id>', views.editPost, name='editPost'),
]