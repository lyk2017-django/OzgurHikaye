from django import forms
from ozgur_modul.models import Storys, Contributions
from django.forms import HiddenInput

class StoryNewForm(forms.ModelForm):
    class Meta:
        model = Storys
        exclude = ["id"]

class ContribituonsNewForm(forms.ModelForm):
    class Meta:
        model = Contributions
        exclude = ["id"]
        widgets = {
            "story": HiddenInput()
        }


#x=ContribituonsNewForm(request.POST)
#x.is_valid()
#x.save()