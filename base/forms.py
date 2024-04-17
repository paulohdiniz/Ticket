from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Customer, User, ProfissionalSaude

class DoctorSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nome", max_length=100)
    password1 = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", strip=False, widget=forms.PasswordInput)
    especialidade = forms.CharField(label="Especialidade", max_length=100)
    registro = forms.CharField(label="Registro", max_length=20)

    class Meta:
        model = User
        fields = ("first_name", "email", "password1", "password2", "especialidade", "registro")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = ProfissionalSaude.objects.create(user=user, especialidade=self.cleaned_data['especialidade'], registro=self.cleaned_data['registro'])
        return user

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nome", max_length=100)
    password1 = forms.CharField(label="Senha", strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user


class FormLogin(forms.Form):
    email = forms.CharField(label ='email')
    password = forms.CharField(label ='senha')
