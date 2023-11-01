from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    gender_choices = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    phone = models.CharField(max_length=15,blank=True,null=True,verbose_name='Номер телефона')
    gender = models.CharField(max_length=1,choices=gender_choices,blank=True,null=True,verbose_name='Пол')
    
    def __str__(self):
        return self.username