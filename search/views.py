from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Institute, Users
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'search/index.html')

def search_institute(request):
    q = request.POST['institution']
    if q:
        object_list = Institute.objects.filter(name__icontains=q)
        html = ""
        for object in object_list:
            html = html + '<div onclick="change_value(this)">'+object.name+'</div>'
    else:
        html = ""
    return HttpResponse(html)

def print_form(request):
    return render(request, 'search/saved.html', {'users': Users.objects.all})

def submit(request):
    try:
        i = Institute.objects.get(name__iexact = request.POST['institution'])
    except ObjectDoesNotExist:
        i = Institute(name = request.POST['institution'])
        i.save()
    q = Users(name = request.POST['name'], institution = i)
    q.save()
    return HttpResponseRedirect(reverse('search:print_form'))
