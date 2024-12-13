from django.urls import path
from usuarios import views    
from django.contrib.auth.views import LogoutView

urlpatterns = [
path("login/",views.login_req,name="login"),
path("registro/",views.registrar,name="registro"),
path("logout/", views.LogoutView.as_view(), name="Logout"),
path("editarperfil/",views.editarPerfil,name="editarperfil"),
path("cambiarcontrasena/",views.CambiarContrasena.as_view(),name="cambiarcontrasena")
]