from django.conf.urls import patterns, include, url

from notyourmotleycrew.content.views import about
from notyourmotleycrew.content.views import thanks 
from notyourmotleycrew.content.views import home 
from notyourmotleycrew.content.views import sign  
from notyourmotleycrew.content.views import sign_pdf
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'notyourmotleycrew.content.views.home', name='home'),
    url(r'^$', home, name='home'),
    url(r'^about/', about, name='about'),
    url(r'^thanks/', thanks, name='thanks'),
    url(r'^contribute/', 'notyourmotleycrew.content.views.contribute', name='contribute'),
    
    url(r'^single_image/(?P<id>\d+)/', 'notyourmotleycrew.content.views.single_image', name='single_image'),
    url(r'^sign/(?P<id>\d+)/', sign, name='sign'),
    url(r'^makesign/', sign, name='makesign'),
    url(r'^sign_pdf/(?P<id>\d+)/', sign_pdf, name='sign_pdf'),

    # url(r'^notyourmotleycrew/', include('notyourmotleycrew.foo.urls')),

     #Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
