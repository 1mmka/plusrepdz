from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main.views import Login,Register,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Register.as_view(),name='register-page'),
    path('login',Login.as_view(),name='login-page'),
    path('home-page',home,name='home')
]
