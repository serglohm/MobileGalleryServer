from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^painters/', GetPainters.as_view()),
)
