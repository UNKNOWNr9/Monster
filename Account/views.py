from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Nasa.models import post
from django.contrib.auth.views import LoginView, PasswordChangeView
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

# registration with Email confirmation

from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from Account.models import User
from django.core.mail import EmailMessage

class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت .'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد. <a href="/login">ورود</a>')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('اکانت شما با موفقیت فعال شد. برای ورود <a href="/login">کلیک</a> کنید.')
    else:
        return HttpResponse('لینک فعال سازی منقضی شده است. <a href="/register">دوباره امتحان کنید.</a>')


