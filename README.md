<h1 align="center"> Fit Sênior </h1>
<p align="center">
    <img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Back-end
<h2>Django</h2>

1. Criar ambiente virtual
   
**conda create -n djangoFitSenior python=3.6**

**conda activate djangoFitSenior**

**pip install -r requirements.txt**

3. Configurar pyCharm e executar o serviço
   
**django-admin startproject fitsenior**

**python manage.py runserver**

**python manage.py startapp paciente**

**python manage.py migrate**

**python manage.py makemigrations paciente**

**pip install psycopg2-binary**

**python manage.py shell**

from paciente.models import Question, Choice

Question.objects.all()

from django.utils import timezone

q = Question(question_text="Teste",pub_date=timezone.now()) 

q.save()

q.question_text

**python manage.py createsuperuser**

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>
