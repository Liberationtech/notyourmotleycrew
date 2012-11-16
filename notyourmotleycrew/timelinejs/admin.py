from notyourmotleycrew.timelinejs.models import Timeline
from notyourmotleycrew.timelinejs.models import TimelineStartdate 
from notyourmotleycrew.timelinejs.models import EventStartdate
from notyourmotleycrew.timelinejs.models import Event
from notyourmotleycrew.timelinejs.models import Argument
from notyourmotleycrew.timelinejs.models import Filterset

from django.contrib import admin

class TimelineStartdateInline(admin.StackedInline):
    model = TimelineStartdate
    max_num = 1

class EventStartdateInline(admin.StackedInline):
    model =  EventStartdate
    max_num = 1


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('headline',)
    inlines = [
            TimelineStartdateInline,
            ]

class ArgumentAdmin(admin.ModelAdmin):
    pass

class FiltersetAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'url', 'headline', 'author', 'media_outlet' , 'facebook_total_count', 'added_by', 'get_startdate' )
    list_filter = ('cleared_for_publication','timeline', 'added_by', 'media_outlet' )
    inlines = [EventStartdateInline,]
    filter_horizontal = ('arguments', 'filtersets')

    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            obj.added_by = request.user
        obj.save()

admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Argument, ArgumentAdmin)
admin.site.register(Filterset, FiltersetAdmin)

