from django.db import models

class Album(models.Model):
    title=models.CharField(max_length=50)
    artist=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    genre=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
