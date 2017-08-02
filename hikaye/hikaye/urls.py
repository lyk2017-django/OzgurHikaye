"""hikaye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from ozgur_modul import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='anasayfa.html'), name='anasayfa'),
    url(r'^storys/$', views.story_list, name='story_list'),
    url(r'^story/create/$', views.story_create, name='story_create'),
    url(r'^story/(?P<pk>\d+)/update/$', views.story_update, name='story_update'),
    url(r'^story/(?P<pk>\d+)/delete/$', views.story_delete, name='story_delete'),
    url(r'^story/(?P<pk>\d+)/like/$', views.story_like, name='story_like'),
    url(r'^story/(?P<pk>\d+)/view/$', views.story_view, name='story_view'),
    url(r'^story/(?P<pk>\d+)/contcreate/$', views.cont_create, name='new_cont_create'),
]
