# Create your tasks here
from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives

from celery import shared_task
from core.models import Projects, InfoNotifications, WarningNotifications



from datetime import *
# import datetime

from django.utils import timezone

from asgiref.sync import async_to_sync
from time import sleep




@shared_task
def sleepy(duration):
    sleep(duration)
    return None


 


@shared_task
def ten_days_left():
    """
    10 gun qalmis notf gedirki proyektin bitmesine 10 gun qalib 

    :return:
    """
    checking_datas = Projects.objects.all()
    for check in checking_datas:
        if check.project_bool == False:
            time_check = date.today() - check.end_time
            if time_check.days == -10:
                InfoNotifications.objects.create(project_name=check,
                                                 notification_type="project_due_date_ten",
                                                 developer=check.developer,
                                                 )

            else:
                print("not this one")
        else:
            print("this developer has fulfillment")

    return "Finished operation"




@shared_task
def five_days_left():
    '''
    proyekte uc gun qalmis notfication gediriki proyekte 5 gun qalib

    :return:
    '''
    checking_datas = Projects.objects.all()
    for check in checking_datas:
        if check.project_bool == False:
            time_check = date.today() - check.end_time
            if time_check.days == -5:
                InfoNotifications.objects.create(project_name=check,
                                                 notification_type="payment_due_date_three",
                                                 developer=check.developer,
                                                 )
                print("yes this one")
            else:
                print("not this one")
        else:
            print("this project has fulfillment")


    return "Finished operation"



@shared_task
def today_is_project_day():
    """
    bu zaman o yaranirki warning olur ve mesaj gedirki proyekt hell olunmalidir. bugun son gundur.
    :return:
    """
    checking_datas = Projects.objects.all()
    for check in checking_datas:
        if check.project_bool == False:
            time_check = date.today() - check.end_time
            if time_check.days == 0:
                WarningNotifications.objects.create(project_name=check,
                                                 notification_type="project_due_date_last",
                                                 developer=check.developer,
                                                 )
                print("yes this one")
            else:
                print("not this one")
        else:

            print("this device has fulfillment")

    return "Finished operation"



@shared_task
def notification_func(email, url):
    subject, from_email, to = "", settings.EMAIL_HOST_USER, email

    html_content = '<p>Change your password with this link <a href="{}">{}</a></p>'.format(
        url + url)
    text_content = ''

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return ""


 



 

 

