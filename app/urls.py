from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('register/', views.registerPage, name='register_page'),
    path('login/', views.loginPage, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.index, name='home_page'),
    path('post_create/', views.createPost, name='post_create'),
    path('post_detail/<int:pk>', views.detailPost, name='detailView'),
    path('post_update/<str:pk>', views.updatePost, name='updateView'),
    path('post_delete/<str:pk>', views.deletePost, name='deleteView'),
]