# encoding=utf-8

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import RedirectView
from django.http import HttpResponse
from tastypie.api import Api
from django.conf.urls import patterns, url, include

from virtrael_api.api import *
from django.views.generic.base import TemplateView


virtrael_api = Api(api_name='virtrael')
virtrael_api.register(ExerciseErrorResource())
# virtrael_api.register(UserResource())

admin.autodiscover()

urlpatterns = patterns('',
                      
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin
                       url(r'^admin/', include(admin.site.urls)),                       
                       (r'^api/', include(virtrael_api.urls)),  
                       #Django
                       (r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       #url(r'^$', RedirectView.as_view(url='/elemental/dashboard/'), name='index'),

)
