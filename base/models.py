from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, password, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        if not password:
            raise ValueError('The password must be set')
        extra_fields.setdefault('is_doctor', False)
        extra_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_doctor', False)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)


        super_user = self._create_user(email, password, **extra_fields)
        return super_user

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USER_TYPE_CHOICES = (
    (1, 'customer'),
    (2, 'profissionalsaude'),
    (3, 'admin'))
    objects = UserManager()
    username = models.CharField(max_length=20, unique=False)
    first_name = models.CharField(max_length=20, unique=False)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=254, unique=True)
    REQUIRED_FIELDS = ['user_type'] # By doing so create superuser command will ask their input


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    idade = models.PositiveIntegerField(null=True)
    endereco = models.CharField(max_length=255,null=True)
    cep = models.CharField(max_length=10,null=True)
    pais = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.first_name

class Ingresso(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False,null=True )
    localizacao = models.CharField(max_length=100, null=True)  # Localização do ingresso
    tipo = models.CharField(max_length=100, null=True)  # Tipo de ingresso
    letra = models.CharField(max_length=10, null=True)  # Campo para letra
    numero = models.PositiveIntegerField(null=True)  # Campo para número
    

    def __str__(self):
        return self.user.first_name
    