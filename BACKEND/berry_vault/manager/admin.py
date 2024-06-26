from django.contrib import admin
from manager.models import Passwords, Vault

# Register your models here.
admin.site.register(Vault)
admin.site.register(Passwords)