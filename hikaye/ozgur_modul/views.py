from django.shortcuts import render, get_object_or_404
from django.db.models import F
from ozgur_modul.models import Storys, Contributions
from ozgur_modul.forms import StoryNewForm, ContribituonsNewForm
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def paginatorReturner(request, ara=""):
    page = request.session["page"]
    siralama = request.session["siralamasi"]

    if ara != "":
        storys = Storys.objects.filter(story_title__contains=ara)
    else: 
        storys = Storys.objects.order_by( siralama )

    paginator = Paginator(storys, settings.SAYFADAKI_KAYIT_ADEDI)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data


def story_list(request,sirala=""):
    if sirala=="":
        sirasi = "id" 
    elif sirala=="title":
        sirasi = "story_title" 
    elif sirala=="date":
        sirasi = "create_time" 
    elif sirala=="view":
        sirasi = "show_count" 
    elif sirala=="like":
        sirasi = "good_count" 
    elif sirala=="dislike":
        sirasi = "bad_count"
    elif sirala=="cont":
        sirasi = "contribution_count"

    page = request.GET.get('page', 1)

    request.session["page"]=page
    if sirasi == request.session["siralamasi"]:
        sirasi = "-" + sirasi
    request.session["siralamasi"]=sirasi

    return render(request, 'ozgur_modul/story_list.html', {'storys': paginatorReturner(request)})


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
            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'storys': paginatorReturner(request)
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

    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': paginatorReturner(request)
    })

    return JsonResponse(data)



def like_update(request, pk):
    data = dict()
    Storys.objects.filter(id=pk).update(good_count=F('good_count') + 1)

    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': paginatorReturner(request)
    })

    return JsonResponse(data)



def dislike_update(request, pk):
    data = dict()
    Storys.objects.filter(id=pk).update(bad_count=F('bad_count') + 1)

    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': paginatorReturner(request)
    })

    return JsonResponse(data)


def cont_create(request, pk):
    if request.method == 'POST':
        yeni_post = request.POST.copy()
        yeni_post["story"] = pk
        form = ContribituonsNewForm(yeni_post)
    else:
        form = ContribituonsNewForm()
    return save_cont_form(request, form, 'ozgur_modul/includes/partial_cont_create.html', pk)


def save_cont_form(request, form, template_name, pk):
    data = dict()
    story = get_object_or_404(Storys, id=pk)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            Storys.objects.filter(id=pk).update(contribution_count=F('contribution_count') + 1)

            data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
                'storys': paginatorReturner(request)
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form,'story_contributions': story.contributions_set.all(), 'story':story}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def arama_sonuc(request):
    data = dict()
    ara  = request.GET.get("aranan_metin", "")

    data['html_story_list'] = render_to_string('ozgur_modul/includes/partial_story_list.html', {
        'storys': paginatorReturner(request, ara)
    })

    return JsonResponse(data)

