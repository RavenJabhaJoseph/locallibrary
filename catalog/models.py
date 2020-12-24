from django.db import models

# Create your models here.
class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (eg.Science, Romance)')

    def __str__(self):
        """String representation"""
        return self.name