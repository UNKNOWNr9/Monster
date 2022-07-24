from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from Nasa.models import post
from django.db.models import Q
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

class SearchBar(ListView):
    template_name = 'WebSite/search-bar.html'
    paginate_by = 5

    def get_queryset(self):
        search = self.request.GET.get('q')
        return post.objects.filter(Q(Description__icontains=search) | Q(Title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context