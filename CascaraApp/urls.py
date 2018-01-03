"""
Definition of urls for CascaraApp.
"""

from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

admin.autodiscover()

urlpatterns = [
    url(r'^', include('getdata.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
]
