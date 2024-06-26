from django.urls import path
from . import views

urlpatterns = [
    path("add_password/",views.Add_password.as_view(), name="Index"),
    path("search/",views.Search.as_view(), name="Create"),
    path("vault/<int:id>/",views.Get_vault.as_view(), name="View_List"),
    path("passwd/<int:id>",views.Get_passwd.as_view(), name="View_List"),
]
