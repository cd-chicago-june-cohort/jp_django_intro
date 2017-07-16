
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def index(request):

    if 'word_list' not in request.session:
        request.session['word_list'] = []

    print "-"*50
    print "from index:   ", request.session['word_list']
    print "-"*50

    return render(request, 'words/index.html')


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def add(request):
    
    if request.method == "POST":
    
        if "new_word" in request.POST:
            name = request.POST["new_word"]
        else: 
            return redirect("/")
        if "color" in request.POST:
            color = request.POST["color"]
        else:
            color = "black"
        size = "regular"
        if "big" in request.POST:
            size = "big"

        new_data = {
            "name": name, 
            "color": color,
            "size": size,
            "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        }

        temp = request.session['word_list']
        print "-"*50
        print "temp starts as:  ", temp
        print "-"*50
        temp.append(new_data)
        print "-"*50
        print "temp after append:  ", temp
        print "-"*50
        request.session['word_list'] = temp

        print "-"*50
        print "after setting session to temp:  ", request.session["word_list"]
        print "-"*50

        return redirect("/")


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def reset(request):
    request.session['word_list'] = []
    return redirect("/")