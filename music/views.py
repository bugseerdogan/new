from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    #Connect database album table
    all_albums = Album.objects.all()
    #context = {'all_albums': all_albums}
    #html= ''
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #   html += '<a href="' + url +'">'+ album.album_title + '</a><br>'
    #return HttpResponse("<h1>This is the music app homepage</h1>")
    return render(request, 'music/index.html' , {'all_albums': all_albums})

def detail(request,album_id):
    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html',{'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song =album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
            'album': album,
            'error_message' : "no selection" ,
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})