from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from manager.models import Vault, Passwords
from .serializer import VaultSerializer, PasswordsSerializer, UserRegisterSerializer, UserLoginSerializer, UserSerializer

from rest_framework.authentication import SessionAuthentication
from manager.validations import custom_validation, validate_email, validate_password
from rest_framework import status
from django.contrib.auth import login, logout


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
	


class MasterPassCheck(APIView):
	"""
	# TODO: Perform an hash check and return a bool depending on the result of the check dddd
	"""
	permission_classes = (IsAuthenticated,)

	def post(self,request, master_pass):
		pass

	



### Handle user from API ###


### Manage Vault ###
class Get_vault(APIView):
	'''get a Vault by his id '''
	permission_classes = (IsAuthenticated,)

	def get(self,request,id):
		try:
			queryset = Vault.objects.get(id=id)
			serializer = VaultSerializer(queryset,many=True)
			return Response(serializer.data)
		except Vault.DoesNotExist:
			return Response({"message": "Vault not found"}, status=status.HTTP_404_NOT_FOUND)
		

class New_vault(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,vault_name):
        if not vault_name:
            return Response({'error': 'Vault name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        vault = Vault.objects.create(user=user, vault_name=vault_name)
        return Response({'message': 'Vault created successfully', 'vault_id': vault.vault_id}, status=status.HTTP_201_CREATED)


## Manage passwords (Add a new password, delete/edit an existing password and get a specific password from an id)
class Add_passwd(APIView):
	permission_classes = (IsAuthenticated,)
	
	def post(self, request):
		data = request.data
		vault_id = data.get('vault_id')
		vault = Vault.objects.get(vault_id=vault_id)
		serializer = PasswordsSerializer(data=data)
		if serializer.is_valid():
			serializer.save(vault=vault)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Edit_passwd(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, pass_name):
		data = request.data
		try:
			password = Passwords.objects.get(pass_name=pass_name)
		except Passwords.DoesNotExist:
			return Response({"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = PasswordsSerializer(password, data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Del_passwd(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):
		pass_name = request.data.get('pass_name')
		try:
			password = Passwords.objects.get(pass_name=pass_name)
		except Passwords.DoesNotExist:
			return Response({"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND)

		password.delete()
		return Response({"message": "Password deleted"}, status=status.HTTP_204_NO_CONTENT)


class Get_passwd(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request, pass_name):
		try:
			password = Passwords.objects.get(pass_name=pass_name)
			serializer = PasswordsSerializer(password)
			return Response(serializer.data)
		except Passwords.DoesNotExist:
			return Response({"message": "Password not found"}, status=status.HTTP_404_NOT_FOUND)