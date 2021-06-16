import datetime
import re
from django.shortcuts import render, get_object_or_404
from atool.models import Universall, Finance, AdvisoryMember, Position
from itertools import chain


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


# Add a new universall database entry
def new_universall(request):
    if request.method == 'POST':
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


def new_finance(request):
    if request.method == 'POST':
        flag = 0
        number = '2020-01-01'
        date = datetime.date.today()
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        reason = request.POST.get('begzantr')
        budget = request.POST.get('haushplan')
        suggestion = request.POST.get('vrshzverf')
        new_fin = Finance(flag, number, date, title, office, name, mail, text, reason, budget, suggestion)
        new_fin.save()
    return render(request, 'stat_html/finance.html')


def new_advisory(request):
    if request.method == 'POST':
        flag = 0
        number = '2020-01-01'
        date = datetime.date.today()
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        frg1 = request.POST.get('frg1')
        frg2 = request.POST.get('frg2')
        frg3 = request.POST.get('frg3')
        frg4 = request.POST.get('frg4')
        new_adv = AdvisoryMember(flag, number, date, title, office, name, mail, text, frg1, frg2, frg3, frg4)
        new_adv.save()
    return render(request, 'stat_html/advisory_member.html')


def new_position(request):
    if request.method == 'POST':
        flag = 0
        number = '2020-01-01'
        date = datetime.date.today()
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        frg1 = request.POST.get('frg1')
        frg2 = request.POST.get('frg2')
        frg3 = request.POST.get('frg3')
        frg4 = request.POST.get('frg4')
        frg_spez_1 = request.POST.get('frg5')
        frg_spez_2 = request.POST.get('frg6')
        frg_spez_3 = request.POST.get('frg7')
        new_pos = Position(flag, number, date, title, office, name, mail, text, frg1, frg2, frg3, frg4, frg_spez_1,
                           frg_spez_2, frg_spez_3)
        new_pos.save()
    return render(request, 'stat_html/election_report.html')


def get_all_by_electioninput(request):
    if request.method == 'POST':
        print(request)
        uni_objects = Universall.objects.all().filter(office=request.POST.get('election_input'))
        fin_objects = Finance.objects.all().filter(office=request.POST.get('election_input'))
        pos_objects = Position.objects.all().filter(office=request.POST.get('election_input'))
        adv_members = AdvisoryMember.objects.all().filter(office=request.POST.get('election_input'))
        if request.POST.get('election_input') == '1':
            office = 'Präsidium'
        if request.POST.get('election_input') == '2':
            office = 'Plenum'
        if request.POST.get('election_input') == '3':
            office = 'Qualitätsmanagement'
        if request.POST.get('election_input') == '4':
            office = 'Testreferat'

        all_objects = chain(uni_objects, fin_objects, pos_objects, adv_members)
        print(all_objects)
        context = {
            'uni_list': all_objects,
            'pos': office
        }
        return render(request, 'intern_out.html', context)
    else:
        return render(request, 'stat_html/intern.html')


def intern_universall(request):
    return render(request, 'get_antrag.html')


def change_universall(request):
    if request.method == 'POST':
        flag = 0
        number = request.POST.get('number')
        date = datetime.date.today()
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        reason = request.POST.get('begzantr')
        suggestion = request.POST.get('vrshzverf')
        mehrheit = request.POST.get('yes')
        beschluss = request.POST.get('beschluss')
        beschlusstext = request.POST.get('bestext')
        beschlussgrund = request.POST.get('begtext')
        new_uni = Universall(flag, number, date, title, office, name, mail, text, reason, suggestion, mehrheit,
                             beschluss, beschlusstext, beschlussgrund)
        new_uni.save()
        return render(request, 'intern_change_uni.html')
    number = request.GET.get('antrag')
    if not number:
        return render(request, 'intern_change_uni.html')
    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    uni_object = get_object_or_404(Universall, number=number)
    context = {
        'uni_object': uni_object
    }
    return render(request, 'intern_change_uni.html', context)


def change_advisory(request):
    if request.method == 'POST':
        flag = 0
        number = request.POST.get('number')
        title = request.POST.get('titel')
        office = request.POST.get('election_input')
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        text = request.POST.get('antrtext')
        reason = request.POST.get('begzantr')
        suggestion = request.POST.get('vrshzverf')
        mehrheit = request.POST.get('yes')
        beschluss = request.POST.get('beschluss')
        beschlusstext = request.POST.get('bestext')
        beschlussgrund = request.POST.get('begtext')
        new_uni = Universall(flag, number, title, office, name, mail, text, reason, suggestion, mehrheit,
                             beschluss, beschlusstext, beschlussgrund)
        new_uni.save()
        return render(request, 'intern_change_uni.html')
    number = request.GET.get('antrag')
    if not number:
        return render(request, 'intern_change_uni.html')
    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    uni_object = get_object_or_404(Universall, number=number)
    context = {
        'uni_object': uni_object
    }
    return render(request, 'intern_change_uni.html', context)