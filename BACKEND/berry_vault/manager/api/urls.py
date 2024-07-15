from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('token/', obtain_auth_token, name="obtain"),

    path("add_password/",views.Add_password.as_view(), name="Index"),
    path("search/",views.Search.as_view(), name="Create"),
    path("vault/",views.Get_vault.as_view(), name="View_List"),
    path("passwd/",views.Get_passwd.as_view(), name="View_List"),
    
    path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
]
