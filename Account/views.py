from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Nasa.models import post
from django.contrib.auth.views import LoginView
from .models import User
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin, AuthorsAccessMixin
from .forms import ProfileForm
# Create your views here.

class PostList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return post.objects.all()
        else:
            return post.objects.filter(author=self.request.user)

class PostCreate(AuthorsAccessMixin, FieldsMixin,FormValidMixin, CreateView):
    model = post
    template_name = 'registration/post-create-update.html'

class PostUpdate(AuthorAccessMixin, FieldsMixin,FormValidMixin, UpdateView):
    model = post
    template_name = 'registration/post-create-update.html'

class PostDelete(SuperUserAccessMixin, DeleteView):
    model = post
    success_url = reverse_lazy('account:home')
    template_name = 'registration/post-confirm-delete.html'

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user' : self.request.user
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')