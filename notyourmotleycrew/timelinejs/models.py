# -*- coding: utf-8 -*-
from django.db import models
import markdown
import json
from django.contrib.auth.models import User

DATE_SPECIFICITY_CHOICE_YEAR = "YEAR"
DATE_SPECIFICITY_CHOICE_MONTH = "MONTH"
DATE_SPECIFICITY_CHOICE_DAY = "DAY"
DATE_SPECIFICITY_CHOICE_HOUR = "HOUR"
DATE_SPECIFICITY_CHOICE_MINUTE = "MINUTE"
DATE_SPECIFICITY_CHOICE_SECOND = "SECOND"


DATE_SPECIFICITY_CHOICES = (
    (DATE_SPECIFICITY_CHOICE_YEAR, DATE_SPECIFICITY_CHOICE_YEAR),
    (DATE_SPECIFICITY_CHOICE_MONTH, DATE_SPECIFICITY_CHOICE_MONTH),
    (DATE_SPECIFICITY_CHOICE_DAY, DATE_SPECIFICITY_CHOICE_DAY),
    (DATE_SPECIFICITY_CHOICE_HOUR, DATE_SPECIFICITY_CHOICE_HOUR),
    #(DATE_SPECIFICITY_CHOICE_MINUTE, DATE_SPECIFICITY_CHOICE_MINUTE),
    #(DATE_SPECIFICITY_CHOICE_SECOND, DATE_SPECIFICITY_CHOICE_SECOND),
  )

# Create your models here.

def escape_text(text):
    text = text.replace('"', "''")
    return json.dumps(markdown.markdown(text))

class Timeline(models.Model):
    headline = models.CharField(max_length = 300)
    type = models.CharField(max_length = 20, default="default")
    text = models.TextField()
    media = models.URLField(blank=True)
    blockquote = models.TextField(blank=True)
    credit = models.CharField(max_length = 400, blank=True) 
    caption = models.CharField(max_length = 400, blank=True)

    def __unicode__(self):
        return u"{0}".format(self.headline)

    def get_json(self):

        datestr = self.startdate.all()[0].json_dumps()
        eventsjson = []
        for event in self.event.filter(cleared_for_publication=True):
            eventsjson.append(event.get_json())
        eventsjsonstr = u",\n".join(eventsjson)

        result = u"""
        {{
        "timeline":
        {{
            "startDate": "{date}",
            "type":"default",
            "headline": "{headline}",
            "text": {text},
            "asset":
            {{
                "media":"{media}",
                "credit":"{credit}",
                "caption":"{caption}"
            }},
        "date": [
        {dates}
        ]
        }}
        }}
        """.format(date=datestr,
                  headline=self.headline,
                  text=escape_text(self.text),
                  media=self.media,
                  credit=self.credit,
                  caption=self.caption,
                  dates=eventsjsonstr)
        return result

def get_oivvio():
    return User.objects.get(id=1)

class Argument(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __unicode__(self):
        return u"{0}".format(self.title)

class Filterset(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{0}".format(self.title)

class Event(models.Model):

    headline = models.CharField(max_length = 300, blank=True, help_text="The headline that is to be displayed on the timeline, NOT the headline of the orignial article. In most cases you do not have to specify this as it's constructed from the AUTHOR and MEDIAOUTLET fields")
    #startdate =  models.DateTimeField()
    #startdate_specificity = models.CharField(max_length=30, choices=DATE_SPECIFICITY_CHOICES, default=DATE_SPECIFICITY_CHOICE_DAY)
    text = models.TextField(blank=True)
    
    blockquote = models.TextField(blank=True)
   
    media = models.URLField(blank=True)
    image = models.ImageField(upload_to="images/timeline/", null=True, blank=True )
    caption = models.CharField(max_length = 400, blank=True, help_text="If you've added an image the caption goes here")
    credit = models.CharField(max_length = 400, blank=True, help_text="If you've added an image the credit for the image goes here") 

    url = models.URLField(blank=True, help_text="Most events should have one")
    media_outlet = models.CharField(max_length = 100, blank=True, help_text="Try to make sure that you use the same spelling and capitalization as previous events in the same outlet")
    author = models.CharField(max_length = 100, blank=True)
        
    
    timeline = models.ForeignKey(Timeline, related_name="event")
    
    facebook_total_count = models.IntegerField(default=-1,editable=False)
    cleared_for_publication = models.BooleanField(default=False)
    added_by = models.ForeignKey(User, related_name="event",  null=True, blank=True, editable=False)

    arguments = models.ManyToManyField(Argument, blank=True)
    filtersets = models.ManyToManyField(Filterset, blank=True)
    
    def get_startdate(self):
        return (self.startdate.get()).datetime

    def get_headline(self):
        if self.headline:
            return self.headline
        elif self.author and self.media_outlet:
            if "blogg" in self.media_outlet:
                prep = u" på "
            else:
                prep = " i "
            return self.author +  prep + self.media_outlet
        else:
            return "Rubbe Rubbe Rubbe"
    
    
    def get_json(self):
        
        
        if self.image:
            media = self.image.url
        elif self.blockquote:
            media = u"<blockquote>{0}</blockquote>".format(self.blockquote)
        else:
            media = self.media
        
        #datestr = get_datestr(self.startdate, self.startdate_specificity)
        datestr = self.startdate.all()[0].json_dumps()

        text = self.text
        translateurl = "http://translate.google.com/translate?sl=sv&tl=en&js=n&prev=_t&hl=sv&ie=UTF-8&layout=2&eotf=1&u={0}".format(self.url)
        if self.facebook_total_count >  0:
            fbcount = "<p>facebook likes: {0}</p>".format(self.facebook_total_count)
        else:
            fbcount = ""

        if self.url:
            text += u"<p><a href='{0}'>länk</a><p> {1} <p><a href='{2}'>google translate</a></p>".format(self.url, fbcount, translateurl)

        #if request.user.is_staff():
            #text += "<p>edit</p>"

        result = u"""
        {{
        "startDate": "{date}",
        "headline": "{headline}",
        "text": {text},
        "asset":
        {{
            "media":"{media}",
            "credit":"{credit}",
            "caption":"{caption}"
        }}
        }}
        """.format(date=datestr, 
                  headline=self.get_headline(),
                  text=escape_text(text),
                  media=media,
                  credit=self.credit,
                  caption=self.caption)
        return result
      


class DateTimeWithSpecificity(models.Model):
    datetime = models.DateTimeField()
    datetime_specificity = models.CharField(max_length=30, choices=DATE_SPECIFICITY_CHOICES, default=DATE_SPECIFICITY_CHOICE_DAY)
    
    def json_dumps(self):
        if self.datetime_specificity == DATE_SPECIFICITY_CHOICE_YEAR:
            return "{0}".format(self.datetime.year)
       
        elif self.datetime_specificity == DATE_SPECIFICITY_CHOICE_MONTH:
            return "{0},{1}".format(self.datetime.year,
                                   self.datetime.month)
        
        elif self.datetime_specificity == DATE_SPECIFICITY_CHOICE_DAY:
            return "{0},{1},{2}".format(self.datetime.year,
                                   self.datetime.month,
                                   self.datetime.day)
            
        elif self.datetime_specificity == DATE_SPECIFICITY_CHOICE_HOUR:
            return "{0},{1},{2},{3}".format(self.datetime.year,
                                   self.datetime.month,
                                   self.datetime.day,
                                   self.datetime.hour)
            
        elif self.datetime_specificity == DATE_SPECIFICITY_CHOICE_MINUTE:
            return "{0},{1},{2},{3},{4}".format(self.datetime.year,
                                   self.datetime.month,
                                   self.datetime.day,
                                   self.datetime.hour,
                                   self.datetime.minute)

class TimelineStartdate(DateTimeWithSpecificity):
    startdate = models.ForeignKey(Timeline, related_name="startdate")


class EventStartdate(DateTimeWithSpecificity):
    startdate = models.ForeignKey(Event, related_name="startdate")





