from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('token/', obtain_auth_token, name="obtain"),
    path("add_password/",views.Add_password.as_view(), name="Index"),
    path("search/",views.Search.as_view(), name="Create"),
    path("vault/",views.Get_vault.as_view(), name="View_List"),
    path("passwd/",views.Get_passwd.as_view(), name="View_List"),
    path("login/",views.Login.as_view(),name="Login"),
    path("register/",views.Register.as_view(),name="Register"),
]
