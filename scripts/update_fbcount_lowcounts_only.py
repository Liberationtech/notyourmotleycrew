from notyourmotleycrew import settings
from notyourmotleycrew.timelinejs.models import Event
import facebook
import json

def run():
    events = Event.objects.all()
    graph = facebook.GraphAPI()
    for event in events:
        
        if event.url != "" and event.facebook_total_count < 5:
            fql = "SELECT total_count FROM link_stat WHERE url='{0}'".format(event.url)
            print fql
            countobject = graph.fql(fql)
            count = countobject[0]["total_count"]
            print count
            if count != event.facebook_total_count:
                event.facebook_total_count = count
                event.save()


        #print event.facebook_total_count

