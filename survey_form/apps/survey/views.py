# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def index(request):
    request.session.clear()
    return render(request, 'survey/index.html')


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def process(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    if request.POST["comment"]:
        request.session["comment"] = request.POST["comment"]
    
    return redirect("/results")


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def results(request):
    return render(request, 'survey/results.html')