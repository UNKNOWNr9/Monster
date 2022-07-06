from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from Nasa.models import post
from django.core.paginator import Paginator
# Create your views here.
class Home(ListView):
    queryset = ''
    template_name = 'WebSite/home.html'
class About(ListView):
    queryset = ''
    template_name = 'WebSite/about.html'

class Contact(ListView):
    queryset = ''
    template_name = 'WebSite/contact.html'


class Post(ListView):
    queryset = post.objects.filter(Status='p').order_by('-Published')
    template_name = 'WebSite/post.html'
    paginate_by = 1


def Nasa_Detail(request, slug):
    context = {
        'obj' : get_object_or_404(post, Slug=slug, Status="p")
    }
    return render(request, 'WebSite/Nasa-Detail.html', context)