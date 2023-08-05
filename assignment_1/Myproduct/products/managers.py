from django.contrib.auth.models import BaseUserManager
from .models import *


class UserManager(BaseUserManager):
    def _create_user(self, email, password,**kwargs):
        if not email:
            raise ValueError('Users must have an Email Address')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_user(self, email, password,**kwargs):
        kwargs.setdefault('is_superuser', False)
        user = self._create_user(email, password, **kwargs)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self._create_user(email, password, **kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
