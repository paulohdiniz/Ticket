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
    profissionais_saude = models.ManyToManyField('ProfissionalSaude')

    def __str__(self):
        return self.user.first_name

class ProfissionalSaude(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_acompanhante = models.BooleanField(default=False)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=20, unique=True,null=True)

    def __str__(self):
        return self.user.first_name
    
class Consulta(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"Consulta {self.local}"

class Chat(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude')
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f"Chat {self.local}"
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    profissionais_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)

    def __str__(self):
        return f"Message {self.chat}"

class Agendamento(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"Agendamento para {self.customer.user.first_name} com {self.profissional_saude.user.first_name} em {self.data} às {self.hora}"