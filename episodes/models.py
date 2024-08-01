from django.db import models

class Episode(models.Model):

    name = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)
    episode_image = models.ImageField(upload_to='episode_image', blank=True, null=True)
    url = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name