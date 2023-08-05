from django.db import models
import uuid
# Create your models here.

class Movie(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False, unique=True)
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title +" -- "+ str(self.id)
