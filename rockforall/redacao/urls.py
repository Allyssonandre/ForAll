from django.urls import path
# IMPORT DAS VIEWS
from . import views
from django.urls import reverse

app_name = 'redacao'
urlpatterns = [
path('filmes/',views.Filmes,name="dicas-filmes"),
]