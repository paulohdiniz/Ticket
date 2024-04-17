
import os, django
import random
from faker import Faker
from itertools import cycle


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FitSenior.settings")  # Substitua 'seu_projeto' pelo nome do seu projeto Django
django.setup()

from base.models import Customer, ProfissionalSaude, Consulta, Chat, Message, User, Agendamento

fake = Faker()

# Criação de instâncias de Customer e ProfissionalSaude com dados fictícios
for _ in range(10):  # Altere o número conforme necessário
    
    user2 = User(
    is_doctor = True,
    user_type = 2,
    first_name=fake.unique.first_name(),
    last_name=fake.unique.last_name(),
    email=fake.email()
    )
    user2.save()
    profissional_saude = ProfissionalSaude(
        user = user2,
        is_acompanhante = fake.boolean(chance_of_getting_true=20),
        especialidade=fake.job(),
        registro=fake.unique.random_number(5, True),
    )
    profissional_saude.save()
    
    
    user = User(
        is_customer = True,
        user_type = 1,
        first_name=fake.unique.first_name(),
        last_name=fake.unique.last_name(),
        email=fake.email()
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
    customer.profissionais_saude.add(profissional_saude)
    customer.save()
    


# Criação de instâncias de Consulta e Chat com dados fictícios
customers_list = list(Customer.objects.all())
profissionais_saude_list = list(ProfissionalSaude.objects.all())

customer_cycle = cycle(customers_list)
profissional_saude_cycle = cycle(profissionais_saude_list)

for _ in range(10):
    consulta = Consulta(
        customer=next(customer_cycle),
        profissional_saude=next(profissional_saude_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        local=fake.address()
    )
    consulta.save()

for _ in range(10):
    chat = Chat(
        customer=next(customer_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        local=fake.address()
    )
    chat.save()

    # Adiciona profissionais aleatórios para cada chat
    chat.profissionais_saude.set([next(profissional_saude_cycle)])
    chat.save()

chat_list = list(Chat.objects.all())
chat_cycle = cycle(chat_list)


for _ in range(100):
    message = Message(
        profissionais_saude=next(profissional_saude_cycle),
        chat=next(chat_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        texto=fake.text(max_nb_chars=500)

    )
    message.save()


# Criar 10 agendamentos
for _ in range(10):
    clientes = list(Customer.objects.all())
    cliente = random.choice(clientes)
    profissional_saude = random.choice(cliente.profissionais_saude.all())
    
    # Gerar dados fictícios para o agendamento
    data = fake.date_between(start_date='-30d', end_date='today')
    hora = fake.time()
    local = fake.address()
    
    # Criar o agendamento
    agendamento = Agendamento.objects.create(
        customer=cliente,
        profissional_saude=profissional_saude,
        data=data,
        hora=hora,
        local=local
    )