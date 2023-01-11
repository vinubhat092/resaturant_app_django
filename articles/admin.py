from django.contrib import admin

# Register your models here.
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','timestamp','updated']
    search_fields = ['title', 'content']

admin.site.register(Articles,ArticleAdmin)
