import datetime
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from Antragsverwaltungstool.models import Universall, Finance, AdvisoryMember, Position, Conduct
from itertools import chain


# This module deals with user requests for files/data and renders the response (HTML-FIlE) with or without
# data out of the database according to the request.

# So far the methods for creating new applications are implemented. As well as the Methods
# for changing applications.

# We also implemented the method to get all entrys by categorie.

# TODOS:
# - Implement deleting
# - Implement show all entrys
# Methods to render the GET requests of the html files
def index(request):
    """ Method to return a HttpResponse with the index.html file when calling the website"""
    return render(request, 'stat_html/index.html')


def finance(request):
    """ Method to return a HttpResponse with the finance.html file when calling / not used """
    return render(request, 'stat_html/finance.html')


def universally(request):
    """ Method to return a HttpResponse with the universally.html file when calling / not used """
    return render(request, 'stat_html/universally.html')


def election(request):
    """ Method to return a HttpResponse with the election_report.html file when calling / not used """
    return render(request, 'stat_html/election_report.html')


def advisory(request):
    """ Method to return a HttpResponse with the advisory_member.html file when calling / not used """
    return render(request, 'stat_html/advisory_member.html')


def intern(request):
    """ Method to return a HttpResponse with the intern.html file when calling / not used """
    return render(request, 'stat_html/intern.html')


def generate_number(object_given):
    """
    Generate the number->primary key for the application ( not implemented yet )

    Parameters:
        object_given (object of type model): The object (application) given, to get
        the last entry in the database.

    """
    number = object_given.objects.first()


def new_universall(request):
    """
    Add a new universall application to the database, with the variables
    extracted out of the post request and the flag 0 for "application arrived".

    Parameters:
        request(WSGIRequest): The request given to the view by the url configuration.
        on which file to be rendered

    Returns:
        a HttpResponse with universally.html.

    """

    if request.method == 'POST':
        # initialize the flag (status) as 0 (eingenagen)
        flag = 0
        number = '2020-01-02'
        # set the date as the current systemdate
        date = datetime.date.today()
        # title of the application
        title = request.POST.get('titel')
        # office the request is pointet to
        office = request.POST.get('election_input')
        # contact data of the applicant
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        # the text of the application
        text = request.POST.get('antrtext')
        # the reason why the application is made
        reason = request.POST.get('begzantr')
        # the suggestion what should be done after the application is processed
        suggestion = request.POST.get('vrshzverf')
        # attachments to the entry
        anlagen = request.POST.get('anlgn')
        # initialize a new object according to the model
        new_uni = Universall(flag, number, date, title, office, name, mail, text, reason, suggestion, anlagen)
        # save the object to the database by calling the django method "save" on the object
        new_uni.save()
        # return the request and the universally.html file
    return render(request, 'stat_html/universally.html')


def new_finance(request):
    """
        Add a new financial application to the database, with the variables
        extracted out of the post request and the flag 0 for "application arrived".

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration
            on which file to be rendered.

        Returns:
            a HttpResponse with finance.html.

    """
    if request.method == 'POST':
        flag = 0
        number = '2020-01-01'
        # set the date as the current systemdate
        date = datetime.date.today()
        # title of the application
        title = request.POST.get('titel')
        # office the request is pointet to
        office = request.POST.get('election_input')
        # contact data of the applicant
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        # the text of the application
        text = request.POST.get('antrtext')
        # the reason why the application is made
        reason = request.POST.get('begzantr')
        # Ammount of money requested by the applicant
        budget = request.POST.get('haushplan')
        # the suggestion what should be done after the application is processed
        suggestion = request.POST.get('vrshzverf')
        # attachments to the entry
        anlagen = request.POST.get('anlgn')
        # initialize a new finance object with the variables
        new_fin = Finance(flag, number, date, title, office, name, mail, text, reason, budget, suggestion, anlagen)
        # call the django method save on the object to write it in the database
        new_fin.save()
    return render(request, 'stat_html/finance.html')


def new_advisory(request):
    """
        Add a application to be voted as a advisory member to the database, with the variables
        extracted out of the post request and the flag 0 for "application arrived".

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration
            on which file to be rendered.

        Returns:
            a HttpResponse with advisory_member.html.

    """
    if request.method == 'POST':
        flag = 0
        print(request)
        number = '2020-01-02'
        # set the date as the current systemdate
        date = datetime.date.today()
        # title of the application
        title = request.POST.get('titel')
        # office the request is pointet to
        office = request.POST.get('election_input')
        # contact data of the applicant
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        # the text of the application
        text = request.POST.get('antrtext')
        # all questions text is displayed by javascript
        # question wether the applicant is in other organisation
        frg1 = request.POST.get('frg1')
        # question about the time investment of the applicant
        frg2 = request.POST.get('frg2')
        # is the applicant willing to put work outside his position
        frg3 = request.POST.get('frg3')
        # how can the applicant support during a zombie apocalypose
        frg4 = request.POST.get('frg4')
        # attachments to the entry
        anlagen = request.POST.get('anlgn')
        # initalize the model object
        new_adv = AdvisoryMember(flag, number, date, title, office, name, mail, text, frg1, frg2, frg3, frg4, anlagen)
        # save it into the databse with django method save
        new_adv.save()
    return render(request, 'stat_html/advisory_member.html')


def new_position(request):
    """
        Add a application to be voted as a special position to the database, with the variables
        extracted out of the post request and the flag 0 for "application arrived".

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration
            on which file to be rendered.

        Returns:
            a HttpResponse with election_report.html.

    """
    if request.method == 'POST':
        flag = 0
        number = '2020-01-01'
        # set the date as the current systemdate
        date = datetime.date.today()
        # title of the application
        title = request.POST.get('titel')
        # office the request is pointet to
        office = request.POST.get('election_input')
        # contact data of the applicant
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        # the text of the application
        text = request.POST.get('antrtext')
        # all questions text is displayed by javascript
        # question wether the applicant is in other organisation
        frg1 = request.POST.get('frg1')
        # question about the time investment of the applicant
        frg2 = request.POST.get('frg2')
        # is the applicant willing to put work outside his position
        frg3 = request.POST.get('frg3')
        # how can the applicant support during a zombie apocalypose
        frg4 = request.POST.get('frg4')
        # Special question when you want to be voted for an office, displayed also by javascript
        # evaluation of the announcement of the position
        frg_spez_1 = request.POST.get('frg5')
        # evaluation of the previous work done by predecessors
        frg_spez_2 = request.POST.get('frg6')
        # what topics does the applicant plan to  put in the foreground in his term of office
        frg_spez_3 = request.POST.get('frg7')
        # attachments to the entry
        anlagen = request.POST.get('anlgn')
        # initialize the object with the vars
        new_pos = Position(flag, number, date, title, office, name, mail, text, frg1, frg2, frg3, frg4, frg_spez_1,
                           frg_spez_2, frg_spez_3, anlagen)
        # save it to the database with django method save
        new_pos.save()
    return render(request, 'stat_html/election_report.html')


def new_conduct(request):
    """
    Add a new establishind conduct application to the database, with the variables
    extracted out of the post request and the flag 0 for "application arrived".

    Parameters:
        request(WSGIRequest): The request given to the view by the url configuration.
        on which file to be rendered

    Returns:
        a HttpResponse with establishing_conduct.html.

    """

    if request.method == 'POST':
        # initialize the flag (status) as 0 (eingenagen)
        flag = 0
        number = '2020-01-02'
        # set the date as the current systemdate
        date = datetime.date.today()
        # title of the application
        title = request.POST.get('titel')
        # office the request is pointet to
        office = request.POST.get('election_input')
        # contact data of the applicant
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        # the text of the application
        text = request.POST.get('antrtext')
        # the reason why the application is made
        reason = request.POST.get('begzantr')
        # the suggestion what should be done after the application is processed
        suggestion = request.POST.get('vrshzverf')
        # attachments to the entry
        anlagen = request.POST.get('anlgn')
        # initialize a new object according to the model
        new_con = Conduct(flag, number, date, title, office, name, mail, text, reason, suggestion, anlagen)
        # save the object to the database by calling the django method "save" on the object
        new_con.save()
        # return the request and the universally.html file
    return render(request, 'stat_html/establishing_conduct.html')


def get_all_by_electioninput(request):
    """
        Display the intern.html site (GET-Request) or get all the applications directed
        to one office put the output on the page.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration
            on which file to be rendered (GET) or the request to display all the applications (POST).
        Returns:
            Returns a HttpResponse with either the normal intern.html (GET) or a
            HttpResponse with the intern.html populated with the context (data from the database).
    """
    if request.method == 'POST':
        # get all objects of every model
        uni_objects = Universall.objects.all().filter(office=request.POST.get('election_input'))
        fin_objects = Finance.objects.all().filter(office=request.POST.get('election_input'))
        pos_objects = Position.objects.all().filter(office=request.POST.get('election_input'))
        adv_members = AdvisoryMember.objects.all().filter(office=request.POST.get('election_input'))
        # office needs to be a string
        office = request.POST.get('election_input')
        # chain all the objects together
        all_objects = chain(uni_objects, fin_objects, pos_objects, adv_members)
        print(all_objects)
        # set the context to the variables out of the database
        context = {
            'uni_list': all_objects,
            'pos': office
        }
        return render(request, 'intern_out.html', context)
    else:
        return render(request, 'stat_html/intern.html')


def common_change(request, object_change, number):
    """
        Generates all the common changes that are always repeated to a given objects.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, POST.

            object_change(model object): THe object that needs to be changed by the function.

            number(string): The number of the application.

        Returns:
              Returns nothing.
    """
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
    object_change.anlagen = request.POST.get('anlgn')
    object_change.aenderung = request.POST.get('aenda')


def change_universall(request):
    """
        Changes an universall application by the variables of the POST-Request. ALl the parameters of the object are
        rendered onto the page before.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, to either get the application,
            or to POST the data and save it to the database.

        Returns:
            Either the HttpRequest with universally_stura.html, or the universally_stura.html populated with content out
            of the database.
    """
    number = request.GET.get('antrag')
    if request.method == 'POST':
        uni_object = get_object_or_404(Universall, number=number)
        common_change(request, uni_object, number)
        uni_object.suggestion = request.POST.get('vrshzverf')
        uni_object.save()

        return render(request, 'stat_html/universally_stura.html')
    # when number is not given render without object
    if not number:
        return render(request, 'stat_html/universally_stura.html')
    # else render with object

    # get the object
    uni_object = get_object_or_404(Universall, number=number)
    context = {
        'uni_object': uni_object
    }
    return render(request, 'stat_html/universally_stura.html', context)


def change_advisory(request):
    """
        Changes an advisory member application by the variables of the POST-Request. ALl the parameters of the object
        are rendered onto the page before.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, to either get the application,
            or to POST the data and save it to the database.

        Returns:
            Either the HttpRequest with advisory_member_stura.html, or the universally_stura.html populated with content
            out of the database.
    """
    number = request.GET.get('antrag')
    if request.method == 'POST':
        advi_object = get_object_or_404(AdvisoryMember, number=number)
        common_change(request, advi_object, number)
        # get the variables of the POST request
        advi_object.frg1 = request.POST.get('frg1')
        advi_object.frg2 = request.POST.get('frg2')
        advi_object.frg3 = request.POST.get('frg3')
        advi_object.frg4 = request.POST.get('frg4')
        advi_object.save()

        return render(request, 'stat_html/advisory_member_stura.html')
    # when number is not given render without object
    if not number:
        return render(request, 'stat_html/advisory_member_stura.html')
    # else render with object
    # get object out of database
    advi_object = get_object_or_404(AdvisoryMember, number=number)
    context = {
        'advi_object': advi_object
    }
    return render(request, 'stat_html/advisory_member_stura.html', context)


def change_position(request):
    """
        Changes an position application by the given variables of the POST-Request. ALl the parameters of the
        object are rendered onto the page before.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, to either get the application,
            or to POST the data and save it to the database.

        Returns:
            Either the HttpRequest with advisory_member_stura.html, or the election_report_stura.html populated with
            content out of the database.
    """
    number = request.GET.get('antrag')
    if request.method == 'POST':
        # get object out of database
        posi_object = get_object_or_404(Position, number=number)
        common_change(request, posi_object, number)
        posi_object.frg1 = request.POST.get('frg1')
        posi_object.frg2 = request.POST.get('frg2')
        posi_object.frg3 = request.POST.get('frg3')
        posi_object.frg4 = request.POST.get('frg4')
        posi_object.frg_spez_1 = request.POST.get('frg5')
        posi_object.frg_spez_2 = request.POST.get('frg6')
        posi_object.frg_spez_3 = request.POST.get('frg7')
        posi_object.save()

        return render(request, 'stat_html/election_report_stura.html')
    if not number:
        return render(request, 'stat_html/election_report_stura.html')
    # matched = re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
    # if re.match("[0-9][0-9][0-9][0-9]/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", number):
    posi_object = get_object_or_404(Position, number=number)
    context = {
        'posi_object': posi_object
    }
    return render(request, 'stat_html/election_report_stura.html', context)


def change_finance(request):
    """
        Changes an finance application by the given variables of the POST-Request. ALl the parameters of the
        object are rendered onto the page before.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, to either get the application,
            or to POST the data and save it to the database.

        Returns:
            Either the HttpRequest with advisory_member_stura.html, or the finance_stura.html populated with content
            out of the database.
    """

    number = request.GET.get('antrag')
    if request.method == 'POST':
        fina_object = get_object_or_404(Finance, number=number)
        common_change(request, fina_object, number)
        fina_object.reason = request.POST.get('begzantr')
        fina_object.budget = request.POST.get('haushplan')
        fina_object.save()

        return render(request, 'stat_html/finance_stura.html')
    # when number is not given render without object
    if not number:
        return render(request, 'stat_html/finance_stura.html')
    # else render with object

    fina_object = get_object_or_404(Finance, number=number)
    context = {
        'fina_object': fina_object
    }
    return render(request, 'stat_html/finance_stura.html', context)


def change_conduct(request):
    """
        Changes an conduct application by the variables of the POST-Request. ALl the parameters of the object are
        rendered onto the page before.

        Parameters:
            request(WSGIRequest): The request given to the view by the url configuration, to either get the application,
            or to POST the data and save it to the database.

        Returns:
            Either the HttpRequest with establishing_conduct_stura.html, or the establishing_conduct_stura.html
            populated with content out of the database.
    """
    number = request.GET.get('antrag')
    if request.method == 'POST':
        con_object = get_object_or_404(Conduct, number=number)
        common_change(request, con_object, number)
        con_object.suggestion = request.POST.get('vrshzverf')
        con_object.save()

        return render(request, 'stat_html/universally_stura.html')
    # when number is not given render without object
    if not number:
        return render(request, 'stat_html/universally_stura.html')
    # else render with object

    # get the object
    con_object = get_object_or_404(Universall, number=number)
    context = {
        'con_object': con_object
    }
    return render(request, 'stat_html/universally_stura.html', context)
