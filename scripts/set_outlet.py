#from notyourmotleycrew import settings
from notyourmotleycrew.timelinejs.models import Outlet
from notyourmotleycrew.timelinejs.models import Event
import facebook
#import json

outlet_string = "Svenska Dagbladet"
outlet = Outlet.objects.filter(name=outlet_string)[0]

def run():
    events = Event.objects.filter(media_outlet=outlet_string)

    for event in events:
        print "-"*10
        event.outlet = outlet
        event.save()
