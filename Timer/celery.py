from __future__ import absolute_import, unicode_literals

import os
from celery.schedules import crontab

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Timer.settings')

app = Celery('Timer',
            include = ['core.tasks']
             )

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


#
# CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
#
# #: Only add pickle to this list if your broker is secured
# #: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
# CELERY_TASK_SERIALIZER = 'json'


if settings.PROD:
    app.conf.update(
        BROKER_URL='amqp://guest:guest@88.99.142.165:5672/',
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='django-db',
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
    )
else:
    app.conf.update(
        BROKER_URL='amqp://guest:guest@localhost:5672/',
        CELERYBEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
        CELERY_RESULT_BACKEND='django-db',
        CELERY_DISABLE_RATE_LIMITS=True,
        CELERY_ACCEPT_CONTENT=['json', ],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',
    )



app.conf.beat_schedule = {
    'last_five_days': {
        'task': "core.tasks.ten_days_left",
        'schedule': crontab(hour=10, minute=10, day_of_week='mon-sun'),
    },
    'last_three_days:': {
        'task': 'core.tasks.five_days_left',
        'schedule': crontab(hour=10, minute=10, day_of_week='0-6'),
    },
    'today_payment_day:': {
        'task': 'core.tasks.today_is_project_day',
        'schedule': crontab(hour=10, minute=10, day_of_week='mon-sun'),
    },
     
}


 