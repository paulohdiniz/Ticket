
import os, django
import random
from faker import Faker
from itertools import cycle


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FitSenior.settings")  # Substitua 'seu_projeto' pelo nome do seu projeto Django
django.setup()

from base.models import Customer, Ingresso, User

fake = Faker()

def gerar_localizacao():
    letra = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numero = random.randint(1, 100)
    return f"{letra}{numero}"

# Criação de instâncias de Customer e ProfissionalSaude com dados fictícios
for _ in range(10):  # Altere o número conforme necessário
    
    user = User(
        is_customer = True,
        user_type = 1,
        username = fake.unique.first_name(),
        first_name=fake.unique.first_name(),
        last_name=fake.unique.last_name(),
        email=fake.unique.email()
    )
    user.save()
    customer = Customer(
        user = user,
        cpf=fake.unique.random_number(9, True),
        idade=random.randint(18, 80),
        endereco=fake.address(),
        cep=fake.zipcode(),
        pais=fake.country(),
    )
    customer.save()
    tipos_ingresso = ['meia-estudante', 'meia-idoso', 'inteira', 'criança', 'premium', 'socio-torcedor']

    for _ in range(1):
        localizacao = gerar_localizacao()
        tipo = random.choice(tipos_ingresso)        
        letra = localizacao[0]
        numero = int(localizacao[1:])
        
        ingresso = Ingresso.objects.create(
            user=user,
            localizacao=localizacao,
            tipo=tipo,
            letra=letra,
            numero=numero
        )
    
