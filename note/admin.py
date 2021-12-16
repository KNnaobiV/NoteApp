from django.contrib import admin
from note.models import Note
# Register your models here

#admin.site.register(Note)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status')
    list_filter = ('author', 'title', 'status')
    search_fields = ('title', 'body')
    date_heirarchy = 'publish'
    ordering = ('status', 'published')
