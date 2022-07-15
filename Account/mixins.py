from django.http import Http404
from django.shortcuts import get_object_or_404
from Nasa.models import post


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = fields = ['author', 'Title', 'Description', 'Image',
                                    'Slug', 'Status', 'Published', 'Category', 'Is_Special'
                                ]
        elif request.user.is_author:
            self.fields = fields = ['Title', 'Description', 'Image',
                                    'Slug', 'Published', 'Category', 'Is_Special'
                                    ]
        else:
            raise Http404("You Dont Have Access To This Page.")
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.Status = 'd'
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        Post = get_object_or_404(post, pk=pk)
        if Post.author == request.user and Post.Status in ['d', 'b'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        else:
            raise Http404("You Dont Have Access To This Page.")


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        else:
            raise Http404("You Dont Have Access To This Page.")