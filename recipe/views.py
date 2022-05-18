
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'nome': 'Alan Barbosa Taborda',
    })

#pasta template o jango ja reconhece automatico
#especificar o caminho para evitar colisão de dados 
# função render vai carregar o arquivo .html