import datetime
import re
from django.shortcuts import render, get_object_or_404
from Antragsverwaltungstool.models import Universall, Finance, AdvisoryMember, Position
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


def generate_number(object_given):
    number = object_given.objects.first()


def common_new(request):
    flag = 0
    number = '2020-01-01'
    date = datetime.date.today()
    title = request.POST.get('titel')
    office = request.POST.get('election_input')
    name = request.POST.get('name')
    mail = request.POST.get('mail')
    text = request.POST.get('antrtext')
    return flag, number, date, title, office, name, mail, text


# Add a new universall database entry
def new_universall(request):
    if request.method == 'POST':
        common_new(request)
        reason = request.POST.get('begzantr')
        suggestion = request.POST.get('vrshzverf')
        new_uni = Universall(common_new(request), reason, suggestion)
        new_uni.save()
    return render(request, 'stat_html/universally.html')


def new_finance(request):
    if request.method == 'POST':
        reason = request.POST.get('begzantr')
        budget = request.POST.get('haushplan')
        suggestion = request.POST.get('vrshzverf')
        new_fin = Finance(common_new(request), reason, budget, suggestion)
        new_fin.save()
    return render(request, 'stat_html/finance.html')


def new_advisory(request):
    if request.method == 'POST':
        frg1 = request.POST.get('frg1')
        frg2 = request.POST.get('frg2')
        frg3 = request.POST.get('frg3')
        frg4 = request.POST.get('frg4')
        new_adv = AdvisoryMember(common_new(request), frg1, frg2, frg3, frg4)
        new_adv.save()
    return render(request, 'stat_html/advisory_member.html')


def new_position(request):
    if request.method == 'POST':
        common_new(request)
        frg1 = request.POST.get('frg1')
        frg2 = request.POST.get('frg2')
        frg3 = request.POST.get('frg3')
        frg4 = request.POST.get('frg4')
        frg_spez_1 = request.POST.get('frg5')
        frg_spez_2 = request.POST.get('frg6')
        frg_spez_3 = request.POST.get('frg7')
        new_pos = Position(common_new(request), frg1, frg2, frg3, frg4, frg_spez_1,
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


def common_change(request, object_change, number):
    object_change.number = number
    object_change.title = request.POST.get('titel')
    object_change.office = request.POST.get('election_input')
    object_change.name = request.POST.get('name')
    object_change.mail = request.POST.get('mail')
    object_change.text = request.POST.get('antrtext')
    object_change.mehrheit = request.POST.get('yes')
    object_change.beschluss = request.POST.get('beschluss')
    object_change.beschlusstext = request.POST.get('bestext')
    object_change.beschlussgrund = request.POST.get('begtext')


def change_universall(request):
    number = request.GET.get('antrag')
    if request.method == 'POST':
        uni_object = get_object_or_404(Universall, number=number)
        common_change(request, uni_object, number)
        uni_object.suggestion = request.POST.get('vrshzverf')
        # uni_object.mehrheit = request.POST.get('yes')
        # uni_object.beschluss = request.POST.get('beschluss')
        # uni_object.beschlusstext = request.POST.get('bestext')
        # uni_object.beschlussgrund = request.POST.get('begtext')
        uni_object.save()

        return render(request, 'intern_change_uni.html')
    # when number is not given render without object
    if not number:
        return render(request, 'intern_change_uni.html')
    # else render with object

    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    # get the object
    uni_object = get_object_or_404(Universall, number=number)
    context = {
        'uni_object': uni_object
    }
    return render(request, 'intern_change_uni.html', context)


def change_advisory(request):
    number = request.GET.get('antrag')
    if request.method == 'POST':
        advi_object = get_object_or_404(AdvisoryMember, number=number)
        common_change(request, advi_object, number)
        advi_object.frg1 = request.POST.get('frg1')
        advi_object.frg2 = request.POST.get('frg2')
        advi_object.frg3 = request.POST.get('frg3')
        advi_object.frg4 = request.POST.get('frg4')
        # advi_object.mehrheit = request.POST.get('yes')
        # advi_object.beschluss = request.POST.get('beschluss')
        # advi_object.beschlusstext = request.POST.get('bestext')
        # advi_object.beschlussgrund = request.POST.get('begtext')
        advi_object.save()

        return render(request, 'intern_change_advisory.html')
    if not number:
        return render(request, 'intern_change_advisory.html')
    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    advi_object = get_object_or_404(AdvisoryMember, number=number)
    context = {
        'advi_object': advi_object
    }
    return render(request, 'intern_change_advisory.html', context)


def change_position(request):
    number = request.GET.get('antrag')
    if request.method == 'POST':
        posi_object = get_object_or_404(Position, number=number)
        common_change(request, posi_object, number)
        posi_object.frg1 = request.POST.get('frg1')
        posi_object.frg2 = request.POST.get('frg2')
        posi_object.frg3 = request.POST.get('frg3')
        posi_object.frg4 = request.POST.get('frg4')
        posi_object.frg_spez_1 = request.POST.get('frg5')
        posi_object.frg_spez_2 = request.POST.get('frg6')
        posi_object.frg_spez_3 = request.POST.get('frg7')
        # posi_object.mehrheit = request.POST.get('yes')
        # posi_object.beschluss = request.POST.get('beschluss')
        # posi_object.beschlusstext = request.POST.get('bestext')
        # posi_object.beschlussgrund = request.POST.get('begtext')
        posi_object.save()

        return render(request, 'intern_change_position.html')
    if not number:
        return render(request, 'intern_change_position.html')
    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    posi_object = get_object_or_404(Position, number=number)
    context = {
        'posi_object': posi_object
    }
    return render(request, 'intern_change_position.html', context)


def change_finance(request):
    number = request.GET.get('antrag')
    if request.method == 'POST':
        fina_object = get_object_or_404(Finance, number=number)
        common_change(request, fina_object, number)
        fina_object.reason = request.POST.get('begzantr')
        fina_object.budget = request.POST.get('haushplan')
        # fina_object.suggestion = request.POST.get('vrshzverf')
        # fina_object.mehrheit = request.POST.get('yes')
        # fina_object.beschluss = request.POST.get('beschluss')
        # fina_object.beschlusstext = request.POST.get('bestext')
        # fina_object.beschlussgrund = request.POST.get('begtext')
        fina_object.save()

        return render(request, 'intern_change_finance.html')
    # when number is not given render without object
    if not number:
        return render(request, 'intern_change_finance.html')
    # else render with object

    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    # get the object
    fina_object = get_object_or_404(Finance, number=number)
    context = {
        'fina_object': fina_object
    }
    return render(request, 'intern_change_finance.html', context)
