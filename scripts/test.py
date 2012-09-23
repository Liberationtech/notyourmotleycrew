# -*- coding: utf-8 -*-
from notyourmotleycrew.timelinejs.models import Event

from notyourmotleycrew.timelinejs.models import Timeline
def run():
    timelines = Timeline.objects.all()
    for timeline in timelines:
        print timeline.get_json()
