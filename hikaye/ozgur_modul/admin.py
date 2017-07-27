from django.contrib import admin
from ozgur_modul.models import Storys, Contributions


#class ShortNewsInline(admin.ModelAdmin):
#    model = Storys.story_title.through
#    extra=0


@admin.register(Storys)
class StorysAdmin(admin.ModelAdmin):
    list_display = ("story_title","create_time")
    list_filter = ("story_title","create_time")
    search_fields = ("story_title", "create_time")


@admin.register(Contributions)
class ContributionsAdmin(admin.ModelAdmin):
    list_display = ("story","contribution_text","create_time")
    list_filter = ("story","contribution_text","create_time")
    search_fields = ("story__story_title","contribution_text","create_time")
#    fieldsets=[("Global",{"fields":["contribution_text"]}),("Dates",{"fields":["create_time"]})]
#    readonly_fields = ["create_time"]