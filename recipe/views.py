
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'recipe/pages/home.html', context={
        'name': 'Alan Barbosa Taborda',
    })





