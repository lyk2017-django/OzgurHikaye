from django.shortcuts import render
from django.views import generic

# Create your views here.

from ozgur_modul.models import Storys, Contributions

class AnaSayfaView(generic.TemplateView):
    template_name = "ozgur_modul/anasayfa.html"

class SSSView(generic.TemplateView):
    template_name = "ozgur_modul/sss.html"

class StoryListView(generic.ListView):
    template_name = "ozgur_modul/hikayeler.html"
    model = Storys
#    def get_queryset(self):
#        return Contributions.objects.all()

class StoryView(generic.DetailView):
    template_name = "ozgur_modul/hikaye.html"
    model = Storys