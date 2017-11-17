from django.db import models
from django.utils import timezone

# Create your models here.

class DataPoint(models.Model):
    time = models.DateTimeField(default=timezone.now)
    category = models.IntegerField()
    data = models.FloatField()
    
#    def __str__(self):
#        return self.time + " " + self.category + " " + self.data