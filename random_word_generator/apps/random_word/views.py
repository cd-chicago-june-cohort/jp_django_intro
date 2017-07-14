

from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.utils.crypto import get_random_string


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def index(request):

    if 'attempt_count' not in request.session:
        request.session['attempt_count'] = 0

    context = {}

    if 'rand_str' in request.session:
        context = {
            "rand_str": request.session["rand_str"]
        }

    return render(request, 'random_word/index.html', context)


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def gen_num(request):
    request.session['attempt_count'] += 1
    request.session['rand_str'] = get_random_string(length=14)
    return redirect('/')


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def reset_attempts(request):
    request.session['attempt_count'] = 0
    del request.session['rand_str']
    return redirect('/')