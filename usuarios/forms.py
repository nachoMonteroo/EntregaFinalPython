from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password=None
    username=forms.CharField(label="nombre de usuario")
    email=forms.EmailField(label="email")
    last_name= forms.CharField(label="apellido")
    first_name=forms.CharField(label="nombre")
    imagen = forms.ImageField(label="Avatar",required=False)

    class Meta:
        model = User
        fields=["username","email","last_name","first_name","imagen"]


class CrearUsuario(UserCreationForm):
    imagen = forms.ImageField(label="Avatar",required=True, initial="../media/defaultimagen.png")
