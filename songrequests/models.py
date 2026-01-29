from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, null=False, default='Single')
    duration = models.DurationField()
    url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class SongRequest(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    requested_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Request for {self.song.title} by {self.requested_by} at {self.requested_at}"