from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Usuário"
            }
        )
    )
    password = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Sua senha"
            }
        )
    )

class RegisterForm(UserCreationForm):
    username=forms.CharField(
        label="Usuário", 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex: joao.silva',
            }
        )
    )
    email=forms.EmailField(
        label="Endereço de e-mail",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex: joao.silva@gmail.com'
            }
        )
    )
    password1 = forms.CharField(label="Senha",
    strip=False,
    widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sua senha'
            }
        )
    )
    password2 = forms.CharField(label="Confirme a senha",
    strip=False,
    widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite novamente sua senha'
            }
        )
    )
            
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2"]
                  