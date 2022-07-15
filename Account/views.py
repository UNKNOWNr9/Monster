from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Nasa.models import post
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
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

class PostUpdate(AuthorAccessMixin, FieldsMixin,FormValidMixin, UpdateView):
    model = post
    template_name = 'registration/post-create-update.html'

class PostDelete(SuperUserAccessMixin, DeleteView):
    model = post
    success_url = reverse_lazy('account:home')
    template_name = 'registration/post-confirm-delete.html'