from django.shortcuts import render, get_object_or_404
from django.db.models import F
from ozgur_modul.models import Storys, Contributions
from ozgur_modul.forms import StoryNewForm, ContribituonsNewForm

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


def story_list(request,sirala=""):
    if sirala=="":
        storys = Storys.objects.all()
    elif sirala=="title":
        storys = Storys.objects.order_by("story_title")
    elif sirala=="date":
        storys = Storys.objects.order_by("-create_time")
    elif sirala=="view":
        storys = Storys.objects.order_by("-show_count")
    elif sirala=="like":
        storys = Storys.objects.order_by("-good_count")
    elif sirala=="dislike":
        storys = Storys.objects.order_by("-bad_count")
    elif sirala=="cont":
        storys = Storys.objects.order_by("contribution_count")
    return render(request, 'ozgur_modul/story_list.html', {'storys': storys})


def story_create(request):
    if request.method == 'POST':
        form = StoryNewForm(request.POST)
    else:
        form = StoryNewForm()
    return save_story_form(request, form, 'ozgur_modul/includes/partial_story_create.html')


def save_story_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            storys = Storys.objects.all()
            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'storys': storys
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def story_update(request, pk):
    pass


def story_delete(request, pk):
    pass


def story_like(request, pk):
    pass


def story_view(request, pk):
    data = dict()
    story = get_object_or_404(Storys, id=pk)

    Storys.objects.filter(id=pk).update(show_count=F('show_count') + 1)

    story.refresh_from_db()
    context = {'story_contributions': story.contributions_set.all(), 'story':story}
    data['html_form'] = render_to_string('ozgur_modul/includes/partial_story_cont_view.html',context, request=request )


    storys = Storys.objects.all()
    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': storys
    })

    return JsonResponse(data)



def like_update(request, pk):
    data = dict()
    Storys.objects.filter(id=pk).update(good_count=F('good_count') + 1)

    storys = Storys.objects.all()
    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': storys
    })

    return JsonResponse(data)



def dislike_update(request, pk):
    data = dict()
    Storys.objects.filter(id=pk).update(bad_count=F('bad_count') + 1)

    storys = Storys.objects.all()
    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': storys
    })

    return JsonResponse(data)


def cont_create(request, pk):
    if request.method == 'POST':
        form = ContribituonsNewForm(request.POST)
    else:
        form = ContribituonsNewForm()
    return save_cont_form(request, form, 'ozgur_modul/includes/partial_cont_create.html', pk)


def save_cont_form(request, form, template_name, pk):
    data = dict()
    story = get_object_or_404(Storys, id=pk)
    if request.method == 'POST':
        form.fields["story"] = story
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            conts = Contributions.objects.all()
            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'conts': conts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'story_contributions': story.contributions_set.all(), 'story':story}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


