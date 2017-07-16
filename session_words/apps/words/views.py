
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def index(request):

    if 'word_list' not in request.session:
        request.session['word_list'] = []

    print "-"*50
    print request.session['word_list']
    print "-"*50

    return render(request, 'words/index.html')


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def add(request):
    
    if request.method == "POST":
    
        # name = request.POST["new_word"]
        # color = request.POST["color"]

        # new_data = {
        #     "name": name, 
        #     "color": color
        # }

        # if 'word_list' not in request.session:
        #     request.session['word_list'] = []

        # request.session['word_list'] = []

        request.session['word_list'].append("cat")

        print "-"*50
        print "from add:  ", request.session["word_list"]
        print "-"*50


        

        # temp = request.session['word_list']
        # print "-"*50
        # print temp
        # print "-"*50
        # temp.insert(0, new_data)
        # print "-"*50
        # print temp
        # print "-"*50
        # request.session['word_list'] = temp
        # print "-"*50
        # print request.session['word_list']
        # print "-"*50
        

        # print "-"*50
        # print "from add:  ", request.session["word_list"]
        # print "-"*50

        return redirect("/")


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def reset(request):
    pass