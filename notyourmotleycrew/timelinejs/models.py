from django.db import models

# Create your models here.

class Timeline(models.Model):
    headline = models.CharField(max_length = 300)
    type = models.CharField(max_length = 20, default="default")
    startdate =  models.DateTimeField()
    text = models.TextField()
    media = models.URLField()
    blockquote = models.TextField()
    credit = models.CharField(max_length = 400) 
    caption = models.CharField(max_length = 400)

class Event(models.Model):
    
    headline = models.CharField(max_length = 300)
    startdate =  models.DateTimeField()
    text = models.TextField()
    media = models.URLField()
    blockquote = models.TextField()
    credit = models.CharField(max_length = 400) 
    caption = models.CharField(max_length = 400)

    timeline = models.ForeignKey(Timeline)

