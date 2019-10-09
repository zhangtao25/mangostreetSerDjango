from django.contrib import admin
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display=('id','created','title','type','desc','likes','cover','collects','images')


admin.site.register(Note, NoteAdmin)