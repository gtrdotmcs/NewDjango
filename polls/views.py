from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    conrlink = """<br/><a href="http://www.freedomain.co.nr/" target="_blank" title="Free Domain Forwarding"><img src="http://umuea.imdrv.net/623/2.gif" width="88" height="31" border="0" alt="Free Domain Forwarding" /></a>"""
    return HttpResponse("Hello, world. You're at the polls index."+conrlink)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
