from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import  Response
from rest_framework.views import APIView
from manager.api.serializer import RegistrationSerializer, PasswordChangeSerializer
from rest_framework import permissions, status



# Create your views here.
