from django.db import models

# Create your models here.
class Album(models.Model):
    #variable names are also column names in db
    artist = models.CharField(max_length=250)
    album_title =  models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model) :
    #on delete var çünkü albümü silersek şarkıda silinsin o albüme ait.
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title =models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    #dont need migration
    def __str__(self):
        return self.song_title