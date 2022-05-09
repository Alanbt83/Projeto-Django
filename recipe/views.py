
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipe/home.html', context={
        'nome': 'Alan Barbosa Taborda',
    })
