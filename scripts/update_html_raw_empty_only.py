#from notyourmotleycrew import settings
from notyourmotleycrew.timelinejs.models import Event
import urllib
def run():
    events = Event.objects.all()
    for event in events:
        if event.url and event.url[-3:] != "pdf":
            print ".",

            if event.html_raw == None:
                print event.url
                try:
                    fh = urllib.urlopen(event.url)
                    event.html_raw = fh.read()
                    event.save()
                except:
                    pass

