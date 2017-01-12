from django.db import models
from .utils import create_shortcode

# Create your models here.

class Paste(models.Model):
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if (self.shortcode is None) or self.shortcode=="":
            self.shortcode=create_shortcode(self)
        super(Paste, self).save(*args, **kwargs)


