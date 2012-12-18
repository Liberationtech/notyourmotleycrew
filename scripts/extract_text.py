#from notyourmotleycrew import settings
from notyourmotleycrew.timelinejs.models import Outlet
from notyourmotleycrew.timelinejs.models import Event
#import json

#outlet_string = "Dagens Nyheter"
#outlet = Outlet.objects.filter(name=outlet_string)[0]

from pyquery import PyQuery

#outlet = Outlet.objects.get(name="Aftonbladet")
#outlet = Outlet.objects.get(name="Dagens Nyheter")
#outlet = Outlet.objects.get(name="Newsmill")
outlet = Outlet.objects.get(name="Svenska Dagbladet")
def run():
    #events = Event.objects.all()
    events = Event.objects.filter(outlet=outlet) 
    for event in events:
        event.populate_text()
        #exit()
