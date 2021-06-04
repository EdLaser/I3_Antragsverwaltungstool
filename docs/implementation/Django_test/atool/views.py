import datetime
from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from .forms import NewUniversallForm

from atool.models import Universall, Finance, AdvisoryMember, Position


def index(request):
    return render(request, 'stat_html/index.html')


def finance(request):
    return render(request, 'stat_html/finance.html')


def universally(request):
    return render(request, 'stat_html/universally.html')


def election(request):
    return render(request, 'stat_html/election_report.html')


def advisory(request):
    return render(request, 'stat_html/advisory_member.html')


def intern(request):
    return render(request, 'stat_html/intern.html')


def new_universall(request):
    if request.method == 'POST':
        print(request.POST)
        flag = 0
        number = '2020-01-01'
        date = datetime.date.today()
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        reason = request.POST.get('begzantr')
        suggestion = request.POST.get('vrshzverf')
        new_uni = Universall(flag, number, date, title, office, name, mail, text, reason, suggestion)
        new_uni.save()
    return render(request, 'stat_html/universally.html')
