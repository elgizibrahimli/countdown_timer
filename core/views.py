from django.shortcuts import render
from core.models import Projects,InfoNotifications,WarningNotifications
from django.http import JsonResponse


from .tasks import sleepy,ten_days_left
from django.views import View


from celery import current_app

from django import forms
from django.conf import settings



"""

def index(reuqest):
    sleepy(10)
    return HttpResponse('Done!')

"""




 



class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)

