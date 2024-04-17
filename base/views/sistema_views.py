from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views import View
from base.models import Ingresso, Customer
from django.contrib.auth import views as auth_views,  authenticate, login
from django.contrib import auth


@login_required
def home(request):
    user = request.user
    ingresso = Ingresso.objects.filter(user=user)
    all = Ingresso.objects.all()
    return render(request, "home.html", {
        'paciente': user,
        'ingressos_do_usuario': ingresso,
        'all' : all
    })

def user_signup(request):
    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect('/')
