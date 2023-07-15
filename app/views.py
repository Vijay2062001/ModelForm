from django.shortcuts import render

# Create your views here.

from app.forms import *


from django.http import HttpResponse

def Insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
            return HttpResponse('Insert Done')
    return render(request,'Topic.html',d)



def Insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid():
            WMFD.save()
            return HttpResponse('Insert Done')
    return render(request,'Webpage.html',d)


def Insert_Access(request):
    ACFO=AccessModelForm()
    d={'ACFO':ACFO}
    if request.method=='POST':
        ACFD=AccessModelForm(request.POST)
        if ACFD.is_valid():
            ACFD.save()
            return HttpResponse('Insert Done')

    return render(request,'access.html',d)

