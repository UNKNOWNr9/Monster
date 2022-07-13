from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Nasa.models import post
from .mixins import FieldsMixin, FormValidMixin
# Create your views here.

class PostList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return post.objects.all()
        else:
            return post.objects.filter(author=self.request.user)

class PostCreate(LoginRequiredMixin, FieldsMixin,FormValidMixin, CreateView):
    model = post
    template_name = 'registration/post-create-update.html'