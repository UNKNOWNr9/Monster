from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Nasa.models import post
# Create your views here.

class home(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'
    queryset = post.objects.all()
