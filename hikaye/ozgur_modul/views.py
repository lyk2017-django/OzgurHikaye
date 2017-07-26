from django.shortcuts import render
from django.views import generic

# Create your views here.

from ozgur_modul.models import Storys, Contributions

class AnaSayfaView(generic.TemplateView):
    template_name = "hikaye/anasayfa.html"

class SSSView(generic.TemplateView):
    template_name = "hikaye/sss.html"

class StoryListView(generic.ListView):
    model = Storys
#    def get_queryset(self):
#        return Contributions.objects.all()

class StoryView(generic.DetailView):
    def get_queryset(self):
        return Contributions.objects.all() #filter(story=pk)


