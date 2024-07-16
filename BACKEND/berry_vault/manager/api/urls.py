from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    # get api token
    path('token/', obtain_auth_token, name="obtain"),


    # handle password/vault
    path("add_password/",views.Add_passwd.as_view(), name="Add_Password"),
    path("edit_password/",views.Edit_passwd.as_view(),name="Edit_Password"),
    path("del_password/",views.Del_passwd.as_view(),name="Del_Password"),
    path("get_passwd/",views.Get_passwd.as_view(), name="Get_Password"),

    path("search/",views.Search.as_view(), name="Search"),
    path("vault/",views.Get_vault.as_view(), name="Vault"),
    
    
    # handle user
    path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
]
