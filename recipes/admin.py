from django.contrib import admin
# from django.contrib.admin.options import TabularInline


# Register your models here.
from .models import RecipeIngredient,Recipe


admin.site.register(RecipeIngredient)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0                            # we can manually add ingrediant to the page
    # fields = ['name','quantity','unit','directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]   # we can configer two models in a single page using inlines
    list_display = ['name','user']
    readonly_fields = ['timestamp','updated']
    raw_id_fields = ['user']
    


admin.site.register(Recipe,RecipeAdmin)