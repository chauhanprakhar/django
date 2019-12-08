from django.db import models

# Create your models here.It automatically creates tables in your database every variable in a  class has different row or column i database table

class album(models.Model):
    artist = models.CharField(max_length=250) #you have to fill data type after . and also max value
    album_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.album_title + '_' + self.artist
        
class song(models.Model):
    album = models.ForeignKey(album , on_delete= models.CASCADE) #forienkey is used to link this class from the class album and on delete cascade is used to 
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)