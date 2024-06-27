from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#### Manage users without using the built-in django methods for more flexibility ####
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
#### Manage users without using the built-in django methods for more flexibility ####


class Vault(models.Model):
    vault_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="vault",null=False)
    vault_name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.vault_name
    

class Passwords(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    pass_name = models.CharField(primary_key=True,max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    site = models.CharField(max_length=255,null=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.pass_name
    
    class Meta:
        verbose_name_plural = "Passwords"