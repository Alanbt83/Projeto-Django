
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'nome': 'Alan Barbosa Taborda',
    })


def contato(request):
    return HttpResponse('Contatos')


def sobre(request):
    return HttpResponse('Sobre')


#pasta template o jango ja reconhece automatico
#especificar o caminho para evitar colisão de dados 
# função render vai carregar o arquivo .html