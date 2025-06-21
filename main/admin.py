from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tag', 'date')
    search_fields = ('title', 'tag')
    list_filter = ('tag', 'date')

admin.site.register(Post, PostAdmin)
