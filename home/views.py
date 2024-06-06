from django.shortcuts import redirect, render

from django.contrib.messages import constants
from django.contrib import messages

from usuario.models import AtivarPesquisaSalas, Sala,Curso,RegistroCurso

from django.urls import reverse
from django.contrib.auth import logout


def home(request):
    status_pesquisa_salas = AtivarPesquisaSalas.objects.all().first().ativado
    
    return render(request,'menu.html',{"status_pesquisa_salas":status_pesquisa_salas})

def pesquisar_sala(request):
    cursos = Curso.objects.all()
    turnos = RegistroCurso.TURNO_CHOICES
    
    
    context = {
        'cursos':cursos,
        'turnos':turnos
    }
    
    if request.method == 'POST':
        semestre = request.POST['semestre']
        curso = request.POST['curso']
        turno = request.POST['turno']
        
        try:
            registro = RegistroCurso.objects.get(curso = curso, turno = turno, semestre = semestre )
            return redirect (reverse('video_sala', kwargs={'id_sala':registro.sala.pk}))
        
        except RegistroCurso.DoesNotExist:
            messages.add_message(request,constants.ERROR,"Registro de curso não encontrado")    

    return render (request,'pesquisarSala.html',context)



def index (request):
    
    return render(request, 'index.html')

def video_sala (request,id_sala):
    sala = Sala.objects.get( pk = id_sala )
    return render (request, 'videoSala.html',{"sala":sala})

def pavilhao (request,numero_pavilhao):
    
    salas = Sala.objects.filter(pavilhao = numero_pavilhao)
    
    return render (request,'pavilhao.html',{'salas':salas,'numero_pavilhao':numero_pavilhao })


def deslogar(request):
    logout(request)
    return redirect("/")