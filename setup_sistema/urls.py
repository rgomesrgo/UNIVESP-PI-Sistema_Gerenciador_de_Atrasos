"""
URL configuration for setup_sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app_gestao import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='app_gestao/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("home/", views.home, name="home"),
    path("cadastrar_alunos/", views.cadastro, name="cadastro"),
    path("registrar_presenca/", views.presenca, name="presenca"),
    path("registrar_atraso/", views.registrar_atraso, name="registrar_atraso"),
    path("relatorio/", views.relatorio, name="relatorio"),
    path('limpar_banco/', views.limpar_banco, name='limpar_banco'),
]
