from django.db import models

class Phone(models.Model):
    title = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    price = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title