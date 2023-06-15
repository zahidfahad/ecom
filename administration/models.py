from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    username = models.CharField(unique=True,db_column='username',max_length=50,verbose_name=_("Username"))
    email = models.EmailField(unique=True,db_column='email',verbose_name=_("Email"))
    contact = models.CharField(unique=True,db_column='contact',verbose_name=_("Contact"),max_length=15)
    
    
    def __str__(self):
        return self.username