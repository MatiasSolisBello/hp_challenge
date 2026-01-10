from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    types = models.JSONField()
    height = models.IntegerField()
    weight = models.IntegerField()
    reversed_name = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name