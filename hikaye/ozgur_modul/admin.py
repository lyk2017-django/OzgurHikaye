from django.contrib import admin
from ozgur_modul.models import Storys, Contributions

#def allStory(self, hikaye):
#    metin=[]
#    for i in hikaye.contribution_text.all():
#        metin.append(i)
#    if metin:
#        return ", ".join(metin)
#    else:
#        return ""


class ContributionInline(admin.StackedInline):
    #Admin panelinde Hikayelerden birine girildiğinde altında ilgili katkıların göünmesini sağladık
    model = Contributions
    extra=0


@admin.register(Storys)
class StorysAdmin(admin.ModelAdmin):
    #Admin panelinde list_display ile veri tabanımızdaki gerekli sütunları listeliyoruz
    #Admin panelinde list_filter filtrelenebilecek sütunları giriyoruz.
    #Admin panelinde arama yapmamızı sağlıyor arayabileceğimiz sütunları girdik.
    list_display = ("story_title","create_time")
    list_filter = ("story_title","create_time")
    search_fields = ("story_title", "create_time")
    inlines = [ContributionInline]

@admin.register(Contributions)
class ContributionsAdmin(admin.ModelAdmin):
    list_display = ("story","contribution_text","create_time")
    list_filter = ("story","contribution_text","create_time")
    search_fields = ("story__story_title","contribution_text","create_time")
#    fieldsets=[("Global",{"fields":["contribution_text","allStory"]}),("Dates",{"fields":["create_time"]})]
#    readonly_fields = ["create_time"]
