from rest_framework import serializers
from manager.models import Vault, Passwords,User

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializing Users
    '''
    class Meta:
        model = User
        fields = ('id','password','')


class VaultSerializer(serializers.ModelSerializer):
    '''
    Serializing Vault
    '''
    class Meta:
        model = Vault
        fields = ('vault_id','user','vault_name')


class PasswordsSerializer(serializers.ModelSerializer):
    '''
    Serializing Passwords
    '''
    class Meta:
        model = Passwords
        fields = ('vault','pass_name','login','password','site','favorite')