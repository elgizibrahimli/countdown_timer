from django.db import models

class Developers(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 )

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    developer = models.ForeignKey(Developers,on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField() 