from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from base.models import Ingresso, Customer
from ..forms import CustomerSignUpForm, FormLogin
from ..models import User

class CustomerSignUpView(CreateView):
    model = User
    form_class =  CustomerSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def custom_login(request):
    if request.method == 'POST':
        form = FormLogin(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirecionar para a página de sucesso, por exemplo
                return redirect('pagina_de_sucesso')
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})
    
    


def getAllDoctors(request): 

	all_doctors = ProfissionalSaude.objects.all()
	return render(request, "especialista.html",
    {
        'all_doctors': all_doctors,
	}
    ) 

def getDoctorByID(request, idDoctor): 
    all_doctors = ProfissionalSaude.objects.all()

    doctor = ProfissionalSaude.objects.get(pk = idDoctor)
	
    return render(request, "especialista.html",
    {
        'all_doctors': doctor,
	}
    )

def setRelationCustomerDoctor(request, idDoctor):
    return render(request, "profissionaissaude.html")

def encontrar_profissionais_de_saude_por_usuario(user):
    try:
        # Encontrar o cliente correspondente ao usuário
        cliente = Customer.objects.get(user=user)
        
        # Acessar os profissionais de saúde relacionados ao cliente
        profissionais_de_saude = cliente.profissionais_saude.all()
        
        return profissionais_de_saude
    except Customer.DoesNotExist:
        # Lidar com o caso em que o cliente não existe
        return None



