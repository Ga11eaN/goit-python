from django.db import models


class Money(models.Model):
    pub_date = models.DateTimeField('date published')
    note_text = models.CharField(max_length=200)
    earnings = models.FloatField(default = 0)
    category = models.CharField(max_length=20, default = 'None')