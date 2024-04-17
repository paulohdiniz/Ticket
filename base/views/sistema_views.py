from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views import View
from base.models import ProfissionalSaude, Customer, Agendamento
from django.contrib.auth import views as auth_views,  authenticate, login
from django.contrib import auth


@login_required
def home(request):
    user = request.user
    return render(request, "home.html", {
        'paciente': user    
    })

def user_signup(request):
    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def criar_agendamento(user, profissional_saude, data, hora, local):
    try:
        # Verificar se o usuário e o profissional de saúde são válidos
        customer = user.customer
        if profissional_saude not in customer.profissionais_saude.all():
            raise ValueError("O profissional de saúde não está relacionado ao usuário.")
        
        # Criar um novo objeto de agendamento
        agendamento = Agendamento.objects.create(
            customer=customer,
            profissional_saude=profissional_saude,
            data=data,
            hora=hora,
            local=local
        )
        
        return agendamento
    except Customer.DoesNotExist:
        # Lidar com o caso em que o cliente não existe
        raise ValueError("O usuário não possui um perfil de cliente.")
    except Exception as e:
        # Lidar com outros erros
        raise ValueError(f"Erro ao criar o agendamento: {str(e)}")
