from django.shortcuts import render
from core.models import Projects,InfoNotifications,WarningNotifications
from django.http import HttpResponse

from .tasks import sleepy,ten_days_left

"""
def index(reuqest):
    sleepy(10)
    return HttpResponse('Done!')

"""

def ten_days(request):
    return HttpResponse('10 gun qalib')


