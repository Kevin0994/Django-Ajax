from django import forms
from .models import Usuario

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','email','password','telefono','fecha_nacimiento']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control',
            'id':'nombreid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
            'id': 'emailid'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',
            'id': 'passwordid'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control',
            'id': 'telefonoid'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control',
            'id': 'fechaid'}),
        }


