
from django.urls import path
from . import views

urlpatterns = [
    path('menu/',views.home, name='home'),
    path('pesquisar_sala/',views.pesquisar_sala, name = 'pesquisar_sala'), 
    path('video_sala/<str:id_sala>/',views.video_sala, name = 'video_sala'),
    path('pavilhao/<str:numero_pavilhao>/',views.pavilhao,name='pavilhao'),
    path('', views.index, name='index'),

]




