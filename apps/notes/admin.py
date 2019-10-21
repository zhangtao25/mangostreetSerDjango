from django.contrib import admin
from notes.models import Note
from notes.models import Image
from notes.models import Like
from notes.models import Collect


class NoteAdmin(admin.ModelAdmin):
    list_display = ('note_id', 'created', 'title', 'type', 'desc', 'likes', 'collects', 'images')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'image','note_id','created')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('like_id', 'created', 'note_id', 'user_id')


class CollectAdmin(admin.ModelAdmin):
    list_display = ('collect_id', 'created', 'note_id', 'user_id')


admin.site.register(Note, NoteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Collect, CollectAdmin)
