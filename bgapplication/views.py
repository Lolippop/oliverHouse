#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from person import Person

#相当于C层的方法
def index(request):
    plist = []
    g = (x * x for x in range(5))
    for n in g:
        plist.append(Person(n,'wuchenqiu','10'))
    context_dict = {'boldmessage' : "I am blod",'plist' : plist}
    return render(request, 'register/index.html', context_dict)
