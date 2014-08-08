from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.

def index(req):
    return render_to_response('main.html', {})


def MainCode(req):
    return render_to_response('main/code.html', {})