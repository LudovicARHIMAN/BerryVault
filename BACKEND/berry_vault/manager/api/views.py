from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from manager.models import Vault, Passwords
from .serializer import VaultSerializer, PasswordsSerializer


##### TODO : Implement user management without using the built-in user manager #####
class Register(APIView):
    pass

class Login(APIView):
    pass
##### TODO : Implement user management without using the built-in user manager #####


class Add_password(APIView):
    # permission_classes = (IsAuthenticated,)
    pass


class Search(APIView):
    # permission_classes = (IsAuthenticated,)
    pass 


class Get_vault(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        queryset = Vault.objects.all()
        serializer = VaultSerializer(queryset,many=True)
        return Response(serializer.data)


class Get_passwd(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        queryset = Passwords.objects.all()
        serializer = PasswordsSerializer(queryset,many=True)
        return Response(serializer.data)