# Generated by Django 3.1.4 on 2020-12-04 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BloodManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodpacket',
            name='name',
        ),
    ]