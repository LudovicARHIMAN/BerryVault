from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid

### Manage users from the api with custom table ###
class AppUserManager(BaseUserManager):
	
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		
		return user
	
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.save()
		
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	objects = AppUserManager()
	
	def __str__(self):
		return self.username
##################################################



### Manage passwords and vault in the database ###
class Vault(models.Model):
    vault_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(AppUser,on_delete=models.CASCADE,related_name="vault",null=True)
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
##################################################
