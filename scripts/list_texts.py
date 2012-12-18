# -*- coding: utf-8 -*-
from notyourmotleycrew.timelinejs.models import Event
from notyourmotleycrew.timelinejs.models import Filterset

def run():
    fs = Filterset.objects.get(title="Ful")
    events = Event.objects.filter(filtersets=fs)
    for event in events:
        try:
            headline = event.text_headline.split(":")[1]
        except:
            headline = event.text_headline
        msg = u"+ {0}, \"{1}\", {2:%y%m%d}, {3}s nätutgåva".format(event.author, headline,  event.startdate_copy, event.outlet.name)
        print msg
