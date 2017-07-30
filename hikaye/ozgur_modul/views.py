from django.shortcuts import render
from django.urls import reverse
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
    model = Storys  # object_list nesnesini gönderir
#    def get_queryset(self):
#        return Contributions.objects.all()

class StoryView(generic.DetailView):
    template_name = "ozgur_modul/hikaye.html"
    model = Storys  # object nesnesini gönderir
    pageCounter = Storys.objects.all()[0] 
    pageCounter.show_count += 1 
    pageCounter.save()    



class ContributionCreateView(generic.CreateView):
    form_class = ContribituonsNewForm
    template_name = "ozgur_modul/contcreate.html"
    success_url = "."

    def hikaye_bilgilerini_getir(self):
        """URL'den gelen ID (pk) bilgine bakarak Story nesnesini çeker"""
        query = Storys.objects.filter(id=self.kwargs["pk"])
        if query.exists():
            return query.get()
        else:
            raise  Http404("Contributions not found")

    def get_form_kwargs(self):
        """Formun POST edilmesi sonrasında kaydederken gerekli olan story_id bağlaması burada yapılır"""
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["story"] = self.hikaye_bilgilerini_getir().id
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs): # Template e giden tüm dictionary burada tutulur
        """Formu veritabanına kaydetme aşamasında bize "URL'den gelen ID (pk) bilgisi gerekiyor."""
        context = super().get_context_data(**kwargs)
        context["object"] = self.hikaye_bilgilerini_getir()
        return context



class NewStoryView(generic.CreateView):
    form_class = StoryNewForm
    template_name = "ozgur_modul/create_story.html"

    def get_success_url(self):
        return  reverse("contribution_create", kwargs={"pk":self.object.id})



