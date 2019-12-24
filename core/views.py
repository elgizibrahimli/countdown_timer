from django.shortcuts import render
from core.models import Projects,InfoNotifications,WarningNotifications
from django.http import HttpResponse

from .tasks import sleepy


def index(reuqest):
    sleepy(10)
    return HttpResponse('Done!')
