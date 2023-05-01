from django.contrib import admin

# Register your models here.
from .models import Articles


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','timestamp','updated']
    search_fields = ['title', 'content']
    raw_id_fields = ['user']
admin.site.register(Articles,ArticleAdmin)
