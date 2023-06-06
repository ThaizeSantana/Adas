from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso')
         


def  login(request):
    if request.method == "GET":   
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request,user)
            return render(request, 'filmes.html')
        else:
            return HttpResponse('Email ou Senha inválidos')




@login_required(login_url="login/")
def filmes(request):
         return render(request, 'filmes.html')


def estrelas(request):
         return render(request, 'estrelas.html')


def kakegurui(request):
         return render(request, 'kakegurui.html')
         
def irmaes(request):
         return render(request, 'irmaes.html')
    

def insecure(request):
         return render(request, 'insecure.html')
    
    