from django.urls import path
from . import views
from .views import RegisterUser, LoginUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', RegisterUser.as_view(), name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logged_out.html'), name='logout'),
]
