from django.shortcuts import render
# IMPORTANDO O FORMULÁRIO USERCREATIONFORM
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    # Cadastrado, e redirecionado para o login
    success_url    = reverse_lazy('login')
    # Template de registro
    template_name = 'registration/register.html'
