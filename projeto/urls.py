
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse('Home 1')


def contato(request):
    return HttpResponse('Contatos')


def sobre(request):
    return HttpResponse('Sobre')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]

