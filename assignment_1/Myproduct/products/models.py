from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import uuid
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name +" -- "+ str(self.id)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_by+')
    modified_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_by+')

    class Meta:
        abstract = True
        
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)
    email = models.EmailField(('email address'),max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email +" -- "+str(self.id) 
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
