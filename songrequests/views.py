from django.shortcuts import render
from .models import Song, SongRequest

def request_song(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        requested_by = request.POST.get('requested_by')

        SongRequest.objects.create(
            song=Song.objects.get(id=song_id),
            requested_by=requested_by
        )

        return render(request, template_name='request_success.html', context={'requested_by': requested_by})
    all_songs = Song.objects.all()

    context = {
        'songs': all_songs
    }

    return render(request, template_name='request.html', context=context)