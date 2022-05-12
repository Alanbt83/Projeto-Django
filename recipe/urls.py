
from django.urls import path

from recipe.urls import home

urlpatterns = [
    path('', home),
]
