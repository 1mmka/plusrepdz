from django.shortcuts import render
from main.models import CustomUser
from django.views.generic import CreateView
from django.urls import reverse_lazy
from main.forms import RegisterForm,LoginForm
from django.contrib.auth.views import LoginView

# Create your views here.
class Register(CreateView):
    form_class = RegisterForm
    model = CustomUser
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    
class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    
def home(request):
    return render(request,'home_page.html')