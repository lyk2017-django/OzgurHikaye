
from django.conf.urls import url
from ozgur_modul.views import AnaSayfaView, SSSView, StoryListView, StoryView

urlpatterns = [
    url(r'^$', AnaSayfaView.as_view(), name="home"),
    url(r'^SSS$', SSSView.as_view(), name="faq_page"),
    url(r'^storys$', StoryListView.as_view(), name="list_storys"),
    url(r'^story/(?P<slug>[A-Za-z0-9\-]+)/(?P<pk>d+)$', StoryView.as_view(), name="story_detail"),
]
