from django.http import Http404

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = fields = ['author', 'Title', 'Description', 'Image',
                                    'Slug', 'Status', 'Published', 'Category'
                                ]
        elif request.user.is_author:
            self.fields = fields = ['Title', 'Description', 'Image',
                                    'Slug', 'Published', 'Category'
                                    ]
        else:
            raise Http404
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