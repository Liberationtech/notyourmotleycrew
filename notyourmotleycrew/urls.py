from django.conf.urls import patterns, include, url

from notyourmotleycrew.content.views import about
from notyourmotleycrew.content.views import thanks 
from notyourmotleycrew.content.views import home 
from notyourmotleycrew.content.views import interventions
from notyourmotleycrew.content.views import intervention
from notyourmotleycrew.content.views import sign  
from notyourmotleycrew.content.views import sign_pdf
from notyourmotleycrew.content.views import thedebate
from notyourmotleycrew.content.views import timeline_data
from notyourmotleycrew.content.views import english_summary_of_the_swedish_debate
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'notyourmotleycrew.content.views.home', name='home'),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^interventions/(?P<slug>.+)', intervention, name='intervention'),
    url(r'^interventions/$', interventions, name='interventions'),
    url(r'^thanks/', thanks, name='thanks'),
    url(r'^timeline_data/filtered/id/(?P<id>\d+)/', timeline_data, name='timelinedata'),
    url(r'^timeline_data/filtered/filterset/(?P<filterset>\w+)/', timeline_data, name='timelinedata'),
    url(r'^timeline_data/$', timeline_data, name='timelinedata'),
    
    url(r'^thedebate/filtered/id/(?P<id>\d+)/', thedebate, name='thedebate'),

    url(r'^thedebate/', thedebate, name='thedebate'),
    url(r'^english_summary/', english_summary_of_the_swedish_debate, name='english_summary_of_the_swedish_debate'),
    url(r'^contribute/', 'notyourmotleycrew.content.views.contribute', name='contribute'),
    
    url(r'^single_image/(?P<id>\d+)/', 'notyourmotleycrew.content.views.single_image', name='single_image'),
    url(r'^sign/(?P<id>\d+)/', sign, name='sign'),
    url(r'^makesign/', sign, name='makesign'),
    url(r'^sign_pdf/(?P<id>\d+)/', sign_pdf, name='sign_pdf'),
    url(r'^kellichlyinesi/',  redirect_to, {'url' : 'https://docs.google.com/document/d/1a2gnYbQf6MnidMhPRYTOVhmC'}),

   
    #url(r'^notyourmotleycrew/', include('notyourmotleycrew.foo.urls')),

    #Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
