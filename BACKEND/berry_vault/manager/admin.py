from django.contrib import admin
from manager.models import Passwords, Vault, AppUser, AppUserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms

# Register your models here.
admin.site.register(Vault)
admin.site.register(Passwords)
admin.site.register(AppUser)