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
        """.format(date=self.startdate.year, 
                  headline=self.headline,
                  text=self.text,
                  media=self.media,
                  credit=self.credit,
                  caption=self.caption,
                  dates=eventsjsonstr)
        return result


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
        result = u"""
        {{
        "startDate": "{date}",
        "headline": "{headline}",
        "text": "{text}",
        "asset":
        {{
            "media":"{media}",
            "credit":"{credit}",
            "caption":"{caption}"
        }}
        }}
        """.format(date=self.startdate.year, 
                  headline=self.headline,
                  text=self.text,
                  media=self.media,
                  credit=self.credit,
                  caption=self.caption)
        return result

