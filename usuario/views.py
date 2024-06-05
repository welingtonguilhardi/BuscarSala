# auth/usuario/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('painel')  # Redireciona para a página do painel após o login
        else:
            return HttpResponse('Login invalido')
    return render(request, 'adm.html')

@login_required(login_url='login')
def painel_view(request):
    
    if request.method == 'POST':
        video = request.POST['video_url']
        sala = request.POST['sala']
        curso = request.POST['curso']
        turma = request.POST['turma']
        
        print(video,sala,curso,turma)
    return render(request, 'painel.html')


def admin_template_view(request):
    # Lógica para renderizar o template admin
    return render(request, 'adm.html', context={})




