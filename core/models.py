from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    types = models.JSONField() #ArrayField
    height = models.IntegerField()
    weight = models.IntegerField()
    reversed_name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.reversed_name = self.name[::-1]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name