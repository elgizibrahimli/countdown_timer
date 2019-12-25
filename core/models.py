from django.db import models
from django.utils import timezone
from django.conf import settings

class Developers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 )
    projects = models.ForeignKey(Projects, on_delete=models.PROTECT)

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    end_date = models.DateTimeField()
    project_bool = models.BooleanField(default=False)
 


class InfoNotifications(models.Model):
    project_name = models.ForeignKey(Projects, related_name='info_notification', on_delete=models.CASCADE)
    types = (
        
        ('project_due_date_ten', 'Proyektin müddətinə 10 gün qalır'),
        ("project_due_date_five", 'Proyektin müddətinə 5 gün qalır'),
    )
    notification_type = models.CharField(max_length=50, choices=types)
    #read_status = models.BooleanField(default=False)

    #user = models.ForeignKey(CreateUser, related_name="info_user", on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} {} ".format(self.project_name.id, self.notification_type)
        

    class Meta:
        verbose_name = "Info Notification"
        verbose_name_plural = "Info Notifications"


    def get_value(self):
        result = ''
         

        if self.notification_type == 'project_due_date_ten':
            result = '{} - proyektin müddətinə 10 gün qalıb'.format(self.project_name.id)

        elif self.notification_type == 'project_due_date_five':
            result = '{} - proyektin müddətinə 5 gün qalıb'.format(self.project_name.id)



        return result

class WarningNotifications(models.Model):
    project_name = models.ForeignKey(Projects, related_name='warning_notification', on_delete=models.CASCADE)
    types = (
        ('pass_project_due_date', 'Proyektin müddətindən keçmişdir'),
        
        ("proyekt_due_date_last", 'Proyekt müddətinin son gunu '),
    
    )
    notification_type = models.CharField(max_length=50, choices=types)
    #read_status = models.BooleanField(default=False)
    #user = models.ForeignKey(CreateUser, related_name="warn_user", on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} {} ".format(self.project_name, self.notification_type)


    class Meta:
        verbose_name = "Warning Notification"
        verbose_name_plural = "Warning Notifications"

    def get_value(self):
        result = ''
        if self.notification_type == 'pass_payment_due_date':
            result = '{} -Proyektin müddətindən keçmişdir'.format(self.project_name.id)
        elif self.notification_type == 'project_due_date_last':
            result = '{} -Proyektin müddətinin son günüdür'.format(self.project_name.id)

        return result






