from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from base import views as core_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
