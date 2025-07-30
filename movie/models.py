from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duración en minutos")
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)  # ← NUEVO

    def __str__(self):
        return self.title
