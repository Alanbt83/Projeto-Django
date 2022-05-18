
from django.urls import path, include

from recipe.urls import home

urlpatterns = [
    path('', home),
]
