from django.db import models

# Create your models here.

class Timeline(models.Model):
    headline = models.CharField(max_length = 300)
    type = models.CharField(max_length = 20, default="default")
    startdate =  models.DateTimeField()
    text = models.TextField()
    media = models.URLField(blank=True)
    blockquote = models.TextField(blank=True)
    credit = models.CharField(max_length = 400, blank=True) 
    caption = models.CharField(max_length = 400, blank=True)

    def get_json(self):
        for event in self.event.all():
            print event

class Event(models.Model):
    
    headline = models.CharField(max_length = 300)
    startdate =  models.DateTimeField()
    text = models.TextField(blank=True)
    media = models.URLField(blank=True)
    blockquote = models.TextField(blank=True)
    credit = models.CharField(max_length = 400, blank=True) 
    caption = models.CharField(max_length = 400, blank=True)

    timeline = models.ForeignKey(Timeline, related_name="event")

    def get_json(self):
        pass
        #TODO

