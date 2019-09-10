
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Action, Choice
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
import datetime


def index(request, week=None):
    if request.method == 'POST':
        week = request.POST.get('week_selection', week)

    if week is None:
        today = timezone.now().today()
        week = today.strftime("%U")
    year = timezone.now().year

    list_weeks = []
    for i in range(1, 53):
        list_weeks.append(get_date_range_from_week(year, i))

    activity_list = Action.objects.filter(pub_date = int(week))
    choice_list = Choice.objects.order_by('pk')
    context = {
        'activity_list': activity_list,
        'choice_list': choice_list,
        'list_weeks': list_weeks
    }
    return render(
        request, template_name='weupdates/index.html', context=context)


def LoginView(request):
    return render(request, 'weupdates/login.html')


def login_action(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('weupdates:index')
            else:
                print("not active")
        else:
            return render(request, 'weupdates/login.html')
    else:
        return render(request, 'weupdates/index.html')


def logout_view(request):
    logout(request)
    return redirect('weupdates:index')


def add(request, choice_id):
    print('\033[36m{}\033[0m'.format(request.method), flush=True)  # cyan
    if request.method == 'POST':
        text = request.POST['activity']
        week = request.POST['selected_week']
        good_or_bad = request.POST.get('goodbad', None)
        if good_or_bad is not None:
            good_or_bad = True
        else: good_or_bad = False
        c = Choice.objects.get(pk=choice_id)
        a = Action(
            choice=c, action_text=text, pub_date=int(week),
            goodbad=good_or_bad, user= request.user)
        a.save()
    return redirect('weupdates:index_with_week', week=week)


def remove(request, activity_id):
    Action.objects.filter(pk=activity_id).delete()
    return HttpResponseRedirect(reverse('weupdates:index'))


def get_date_range_from_week(p_year, p_week):
    first_day_of_week = datetime.datetime.strptime(f'{p_year}-W{int(p_week) - 1}-1', "%Y-W%W-%w").date()
    last_day_of_week = first_day_of_week + datetime.timedelta(days=6.9)
    return p_week, first_day_of_week.strftime('%Y-%m-%d'), last_day_of_week.strftime('%Y-%m-%d')


# class IndexView(View):
#     year = timezone.now().year
#     model = Action, Choice
#     list_weeks = []
#
#     for i in range(1, 53):
#         list_weeks.append(get_date_range_from_week(year, i))
#
#     template_name = 'weupdates/index.html'
#     context_object_name =  'activity_list', 'choice_list', 'list_weeks'
#
#     def get(self, request, week):
#         return Choice.objects.order_by('pk'), Action.objects.filter(pub_date__week = week), list_weeks
#
#     def post(self, *arg, **kwargs):
#         pass
#
#     def delete(self, *args, **kwargs):
#         pass
