from notyourmotleycrew import settings
from notyourmotleycrew.timelinejs.models import Event

def run():
    events = Event.objects.all()
    for event in events:
        
        if event.url != "":
            print event.url
            #if count != event.facebook_total_count:
            #    event.facebook_total_count = count
            #    event.save()
