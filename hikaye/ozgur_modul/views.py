from django.shortcuts import render
from django.views import generic
from django.http import  Http404
from ozgur_modul.forms import ContribituonsNewForm, StoryNewForm
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

class ContributionCreateView(generic.CreateView):
    form_class = ContribituonsNewForm
    template_name = "ozgur_modul/contcreate.html"
    model = Contributions

    def get_contributions(self):
        query = Contributions.objects.filter(id=self.kwargs["pk"])
        if query.exists():
            return query.get()
        else:
            raise  Http404("Contributions not found")

    def get_from_kwargs(self):
        kwargs = super().get_form_kwargs()
        post_data = kwargs["data"].copy()
        post_data["storys"]= self.context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"]=self.get_contributions()
        return context

class NewStoryView(generic.CreateView):
    model = Storys
    success_url = "."
    exclute=["id"]
    template_name = "ozgur_modul/create_story.html"
    fields = ["story_title"]
