from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from usuarios.forms import UserEditForm,CrearUsuario
from django.views.generic import View
from usuarios.models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#------------------------------------------------LOGIN,LOGOUT Y REGISTRO---------------------------------------------


def login_req(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")

            user = authenticate(username=usuario,password=contrasena)

            if user is not None:
                login(req,user)
                mensaje = "Hola " + usuario 
                return render(req, "aplicacion/index.html",{"mensaje":mensaje})
            else:
                render(req,"aplicacion/index.html",{"mensaje":"datos erroneos"})
        else:
            return render(req, "usuarios/login.html",{"form":form})
    form = AuthenticationForm()

    return render(req,"usuarios/login.html",{"form":form})




def registrar(req):
    if req.method == "POST":
        form = CrearUsuario(req.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            mensaje = "Hola " + username + "!"
            imagendefault(username)
            return render(req, "aplicacion/index.html",{"mensaje":mensaje})

    else:
        form = CrearUsuario()

    return render(req, "usuarios/registro.html",{"form":form})

def imagendefault(username):
    usuario = User.objects.get(username=username)
    avatar = Avatar(user=usuario,imagen="../media/defaultimagen.png")
    avatar.save()

def editarPerfil(req):
    usuario = req.user
    if req.method =="POST":
        miFormulario = UserEditForm(req.POST,req.FILES,instance=req.user)
        if miFormulario.is_valid():
            miFormulario.save()

            if miFormulario.cleaned_data.get("imagen"):
                usuario.avatar.imagen= miFormulario.cleaned_data.get("imagen")
                usuario.avatar.save()

            return render(req, "aplicacion/index.html")
        
    else:
        miFormulario = UserEditForm(initial={"imagen":usuario.avatar.imagen},instance=req.user)

    return render(req, "usuarios/editarperfil.html",{"miFormulario":miFormulario,"usuario":usuario})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
    
class CambiarContrasena(LoginRequiredMixin,PasswordChangeView):
    template_name="usuarios/cambiarcontrasena.html"
    success_url = reverse_lazy("editarperfil")