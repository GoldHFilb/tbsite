from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 't_price')
    list_display_links = ('id', 'short_name')
    search_fields = ('short_name', 'content')


admin.site.register(Article, ArticleAdmin)
