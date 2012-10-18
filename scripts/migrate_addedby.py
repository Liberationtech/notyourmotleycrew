from notyourmotleycrew.timelinejs.models import Event
from notyourmotleycrew.timelinejs.models import get_oivvio

oivvio = get_oivvio()

def run():
    for event in Event.objects.all():
        print event.url
        event.added_by = oivvio
        event.save()
