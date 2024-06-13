from rest_framework import serializers
from main.models import Vault, Passwords



class VaultSerializer(serializers.ModelSerializer):
    '''
    Serializing Vault
    '''
    class Meta:
        model = Vault
        fields = ('vault_id','user','vault_name')

class Passwords(serializers.ModelSerializer):
    '''
    Serializing Passwords
    '''
    

