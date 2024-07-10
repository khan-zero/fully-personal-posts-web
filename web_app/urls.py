from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('log_out/', views.log_out, name='log_out'),
    path('archive/', views.archive, name='archive'),
    path('contact/', views.contact, name='archive'),
    path('profile/<int:id>', views.profile_card, name='profile'),
]
