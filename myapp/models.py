from django.db import models

# Create your models here.


class Image(models.Model):
    Photo = models.ImageField(upload_to="myimage")
    Date = models.DateTimeField(auto_now_add=True)