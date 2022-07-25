from django.db import models
import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        return f'Titulo: {self.title} - Descripcion: {self.description}  {self.image} {self.date}'



class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True) 