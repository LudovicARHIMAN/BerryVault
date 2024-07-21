from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    # get api token
    path('token/', obtain_auth_token, name="obtain"),


    # handle password
    path("add_password/",views.Add_passwd.as_view(), name="Add_Password"),
    path("edit_password/<str:pass_name>/",views.Edit_passwd.as_view(),name="Edit_Password"),
    path("del_password/<str:pass_name>/",views.Del_passwd.as_view(),name="Del_Password"),
    path("get_passwd/<str:pass_name>/",views.Get_passwd.as_view(), name="Get_Password"),

    # handle vault
    path("get_vault/<int:id>/",views.Get_vault.as_view(), name="Get_Vault"),
    path("new_vault/<str:vault_name>/",views.New_vault.as_view(), name="New_Vault"),
    
    
    # handle user
    path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
]
