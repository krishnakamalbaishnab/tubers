from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitile = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    # this is gonaa create a new a folder called slider and the images will be saved there and %y means the year tge images is created
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
