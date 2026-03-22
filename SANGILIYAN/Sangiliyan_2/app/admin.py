from django.contrib import admin
from .models import Post, Section

class SectionInline(admin.TabularInline):
    model = Section
    extra = 1 # Propose une case vide par défaut

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SectionInline] # Permet d'ajouter les onglets direct dans l'article