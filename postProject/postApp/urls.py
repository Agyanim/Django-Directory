from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('post/create-post',views.createPost, name='createPost'),
    path('posts/', views.posts, name='posts'),
    path('logout/',views.logout, name='logout'),
    path('posts/<str:id>/',views.editPost,name='editPost'),
]