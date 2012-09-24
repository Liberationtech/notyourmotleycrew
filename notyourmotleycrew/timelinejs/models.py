from django.db import models
import markdown
import json

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
    (DATE_SPECIFICITY_CHOICE_MINUTE, DATE_SPECIFICITY_CHOICE_MINUTE),
    (DATE_SPECIFICITY_CHOICE_SECOND, DATE_SPECIFICITY_CHOICE_SECOND),
  )

# Create your models here.

def escape_text(text):
    return json.dumps(markdown.markdown(text))




class Timeline(models.Model):
    headline = models.CharField(max_length = 300)
    type = models.CharField(max_length = 20, default="default")
    text = models.TextField()
    media = models.URLField(blank=True)
    blockquote = models.TextField(blank=True)
    credit = models.CharField(max_length = 400, blank=True) 
    caption = models.CharField(max_length = 400, blank=True)

    
    def get_json(self):

        datestr = self.startdate.all()[0].json_dumps()
        eventsjson = []
        for event in self.event.all():
            eventsjson.append(event.get_json())
        eventsjsonstr = u",\n".join(eventsjson)
        

        result = u"""
        {{
        "timeline":
        {{
            "startDate": "{date}",
            "type":"default",
            "headline": "{headline}",
            "text": "{text}",
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
                  text=self.text,
                  media=self.media,
                  credit=self.credit,
                  caption=self.caption,
                  dates=eventsjsonstr)
        return result


class Event(models.Model):
    headline = models.CharField(max_length = 300)
    #startdate =  models.DateTimeField()
    #startdate_specificity = models.CharField(max_length=30, choices=DATE_SPECIFICITY_CHOICES, default=DATE_SPECIFICITY_CHOICE_DAY)
    text = models.TextField(blank=True)
    media = models.URLField(blank=True)
    blockquote = models.TextField(blank=True)
    credit = models.CharField(max_length = 400, blank=True) 
    caption = models.CharField(max_length = 400, blank=True)
   
    
    image = models.ImageField(upload_to="images/timeline/", null=True)
    timeline = models.ForeignKey(Timeline, related_name="event")

    
    def get_json(self):
        
        
        if self.image:
            media = self.image.url
        else:
            media = self.media
        
        #datestr = get_datestr(self.startdate, self.startdate_specificity)
        datestr = self.startdate.all()[0].json_dumps()
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
                  headline=self.headline,
                  text=escape_text(self.text),
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
        return "2012, 09"

class TimelineStartdate(DateTimeWithSpecificity):
    startdate = models.ForeignKey(Timeline, related_name="startdate")


class EventStartdate(DateTimeWithSpecificity):
    startdate = models.ForeignKey(Event, related_name="startdate")




