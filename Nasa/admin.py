from django.contrib import admin
from Nasa.models import post, PostCategory
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Slug', 'Status', 'Position')
    list_filter = ('Status',)
    search_fields = ('Title', 'Status')


admin.site.register(PostCategory, CategoryAdmin)


@admin.action(description='انتشار پست های انتخاب شده')
def make_published(modeladmin, request, queryset):
    queryset.update(Status='p')

@admin.action(description='پیشنویس پست های انتخاب شده')
def make_draft(modeladmin, request, queryset):
    queryset.update(Status='d')


class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'thumbnail_tag', 'author', 'Slug', 'Status', 'Published')
    list_filter = ('Title', 'Status')
    search_fields = ('Title',)
    ordering = ('Status', '-Published')
    actions = [make_published, make_draft]

admin.site.register(post, PostAdmin)