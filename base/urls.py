from django.conf.urls import include
from django.urls import include, path
from django.contrib.auth import views as auth_views,  authenticate, login


from . import views 

urlpatterns = [ 
	path("", views.home, name="home"), 
    #path('accounts/login/', views.login, name='login'), 
    path('accounts/', include('django.contrib.auth.urls')), #include /login etc
    path('accounts/signup/', views.user_signup, name='user_signup'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/signup/doctor/', views.DoctorSignUpView.as_view(), name='doctor_signup'),
    path('accounts/signup/customer/', views.CustomerSignUpView.as_view(), name='customer_signup'),
    #path('logout', views.LogoutView.as_view(), name='logout'),
    path("ProfissionaisSaude/", views.getAllDoctors),
    path("ProfissionaisSaude/<int:idDoctor>/", views.getDoctorByID),
]
