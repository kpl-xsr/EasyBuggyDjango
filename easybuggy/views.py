from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from django.utils.translation import ugettext as _

def index(request):
    return render(request, 'index.html')


def infiniteloop(request):
    i = 1
    while 0 < i:
        i += 1
    return render(request, 'index.html')


def xss(request):
    d = {
        'title': _('title.xss.page'),
        'msg': _('msg.enter.string'),
    }
    return render(request, 'xss.html', d)