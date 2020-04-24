from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm