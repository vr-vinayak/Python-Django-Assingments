from django.contrib import admin
from .models import Product, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'is_superuser']

# Register your models here.

admin.site.register(Product)
admin.site.register(User, UserAdmin)
