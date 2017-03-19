"""djangov2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from polls import views
from polls.backends import MyRegistrationView


urlpatterns = [

    url(r'^accounts/register/$', 
        MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_thing/$', views.create_thing, 
        name='registration_create_thing'),
    url(r'^$', views.index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^browse/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^browse/name/$',
        views.browse_by_name, name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', 
        views.browse_by_name, name='browse_by_name'),
    url(r'^things/$', RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^things/(?P<slug>[-\w]+)/$', views.thing_detail, 
        name='thing_detail'),
    url(r'^things/(?P<slug>[-\w]+)/edit/$', 
        views.edit_thing,
        name='edit_thing'),
    url(r'^accounts/', 
        include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]