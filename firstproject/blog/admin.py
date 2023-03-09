from django.contrib import admin
from blog.models import Post


# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'update', 'timestamp', 'link_field', 'image',)
    list_display_links = ('title',)
    list_editable = ('content', )
    list_filter = ('update', 'timestamp')
    search_fields = ('title', 'content',)
    list_per_page = 5


admin.site.register(Post, PostModelAdmin)
