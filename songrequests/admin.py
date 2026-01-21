from django.contrib import admin

from .models import Song, SongRequest

admin.site.register(Song)
admin.site.register(SongRequest)