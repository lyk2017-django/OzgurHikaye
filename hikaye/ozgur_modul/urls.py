from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from ozgur_modul import views

urlpatterns=[
    url(r'^$', views.story_list, name='story_list'),
    url(r'^about$', TemplateView.as_view(template_name='hakkimizda.html'), name='about'),
    url(r'^create/$', views.story_create, name='story_create'),
    url(r'^(?P<pk>\d+)/update/$', views.story_update, name='story_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.story_delete, name='story_delete'),
    url(r'^sort/(?P<sirala>\w+)/$', views.story_list, name='sort_list'),
    url(r'^(?P<pk>\d+)/view/$', views.story_view, name='story_view'),
    url(r'^(?P<pk>\d+)/contcreate/$', views.cont_create, name='new_cont_create'),
    url(r'^(?P<pk>\d+)/like/$', views.like_update, name='story_update_like'),
    url(r'^(?P<pk>\d+)/dislike/$', views.dislike_update, name='story_update_dislike'),
    url(r'^search/$', views.arama_sonuc, name='arama_yap'),
]