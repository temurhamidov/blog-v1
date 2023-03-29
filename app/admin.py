from django.contrib import admin
from .models import Category, Tag, Blog, Comment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)