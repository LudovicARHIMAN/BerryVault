from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Vault(models.Model):
    vault_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="vault",null=False)
    vault_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Passwords(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    pass_name = models.CharField(primary_key=True,max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.pass_name