from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def indexView(request):
    return HttpResponse(render(request, 'index.html'))


def rulesView(request):
    return HttpResponse(render(request, 'rules.html'))


def notablesDetail(request):
    return HttpResponse(render(request, 'notablesDetail.html'))


def notablesList(request):
    return HttpResponse(render(request, 'notables.html'))


def externalLinks(request):
    return HttpResponse(render(request, 'externalLinks.html'))