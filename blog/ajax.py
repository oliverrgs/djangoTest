import json
from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf # csrf - cross site request forgery.
from django_ajax.decorators import ajax

@ajax
def sayHello(request):
    print("hi");
    return 'a'