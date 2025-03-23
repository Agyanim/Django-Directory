from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('post/create-post/',views.createPost, name='createPost'),
    path('posts/', views.posts, name='posts'),
]