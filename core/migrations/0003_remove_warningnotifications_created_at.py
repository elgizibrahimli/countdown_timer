# Generated by Django 3.0.1 on 2019-12-23 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_infonotifications_warningnotifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warningnotifications',
            name='created_at',
        ),
    ]