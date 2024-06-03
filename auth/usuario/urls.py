# auth/usuario/urls.py
from django.urls import path
from . import views
from .views import admin_template_view


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('painel/', views.painel_view, name='painel'),
    path('adm/templetes/adm/', admin_template_view, name='admin_template'),
]



