from django import forms

class estudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    ano = forms.IntegerField()
    division = forms.CharField(max_length=1)
    inasistencias = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha_de_nacimiento=forms.DateField()
    email=forms.EmailField()

class profesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    inasistencias = forms.DecimalField(max_digits=3,decimal_places=1)
    fecha_de_nacimiento=forms.DateField()
    email=forms.EmailField()