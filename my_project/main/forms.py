from django.contrib.auth.forms import UserCreationForm
from django import forms
from main.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15,required=True,widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Номер телефона'}),
                            label='Номер телефона')
    gender = forms.ChoiceField(choices=CustomUser.gender_choices,required=True,
        widget=forms.Select(attrs={'class':'form-select'}),label='Пол')
    
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class':'form-control',
                                                'placeholder':'Повторите пароль'}))
    
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя пользователя'})
    )
    
    class Meta:
        model = CustomUser
        fields = ('username','password1','password2','phone','gender')
        
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username','password')
        
    