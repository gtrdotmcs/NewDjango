'''
Created on Jan 24, 2014

@author: ghanshyam
'''

from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, world. You're at the main index.<h1>")
