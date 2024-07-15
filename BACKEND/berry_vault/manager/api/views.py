from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from manager.models import Vault, Passwords
from .serializer import VaultSerializer, PasswordsSerializer, UserRegisterSerializer, UserLoginSerializer, UserSerializer

from rest_framework.authentication import SessionAuthentication
from manager.validations import custom_validation, validate_email, validate_password
from rest_framework import status
from django.contrib.auth import get_user_model, login, logout


### Handle user from API ###
class UserRegister(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (AllowAny,)
	authentication_classes = ()
	
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
### Handle user from API ###



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
    

