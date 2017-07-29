
from django.conf.urls import url
from ozgur_modul.views import AnaSayfaView, SSSView, StoryListView, StoryView, ContributionCreateView, NewStoryView

urlpatterns = [
    url(r'^$', AnaSayfaView.as_view(), name="home"),
    url(r'^SSS$', SSSView.as_view(), name="faq_page"),
    url(r'^storys$', StoryListView.as_view(), name="list_storys"),
    url(r'^story/(?P<pk>\d+)$', StoryView.as_view(), name="story_detail"),
    url(r'^contcreate/(?P<pk>\d+)/$', ContributionCreateView.as_view(), name="contribution_create"),
    url(r'^createstory/$', NewStoryView.as_view(), name="create_story"),
#    url(r'^story/(?P<slug>[A-Za-z0-9\-]+)/(?P<pk>d+)$', StoryView.as_view(), name="story_detail"),
]
