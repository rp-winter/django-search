from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Institute, Users
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from difflib import SequenceMatcher

# Create your views here.

def index(request):
    return render(request, 'search/index.html')

def search_institute(request):
    q = request.POST['institution']
    if q:
        object_list = Institute.objects.filter(name__istartswith=q)
        html = ""
        for object in object_list:
            html = html + '<div onclick="change_value(this)">'+object.name+'</div>'
    else:
        html = ""
    return HttpResponse(html)

def validate_password1(request):
    password1 = request.POST['password1']
    username = request.POST['username']
    fname = request.POST['first_name']
    lname = request.POST['last_name']
    email = request.POST['email']
    html = ""
    user_attribute = (username, fname, lname, email)
    similar = False
    for value in user_attribute:
        if not value or not isinstance(value, str):
                continue
        value_parts = re.split(r'\W+', value) + [value]
        for value_part in value_parts:
            if SequenceMatcher(a=password1.lower(), b=value_part.lower()).quick_ratio() >= 0.7:
                similar = True
    if similar:
        html = html + '<li>Your password can’t be too similar to your other personal information.</li>'
    try:
        validate_password(password1)
    except ValidationError as errors:
        for error in errors:
            html = html + '<li>'+error+'</li>'
    return HttpResponse(html)

def print_form(request):
    return render(request, 'search/saved.html', {'users': Users.objects.all})

def submit(request):
    try:
        i = Institute.objects.get(name__iexact = request.POST['institution'])
    except ObjectDoesNotExist:
        i = Institute(name = request.POST['institution'])
        i.save()
    q = Users(name = request.POST['first_name'], institution = i)
    q.save()
    return HttpResponseRedirect(reverse('search:print_form'))
