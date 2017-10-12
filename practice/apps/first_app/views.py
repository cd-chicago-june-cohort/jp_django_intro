# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = 'Hello, I am your first request.'
    return HttpResponse(response)

def new(request):
    response = "Placeholder for new."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, parameter):
    response = "Placeholder for number " + parameter
    return HttpResponse(response)