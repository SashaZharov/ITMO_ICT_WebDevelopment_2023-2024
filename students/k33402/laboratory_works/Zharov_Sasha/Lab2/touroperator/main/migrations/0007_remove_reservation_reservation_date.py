# Generated by Django 4.2.6 on 2023-10-28 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_reservation_end_date_reservation_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_date',
        ),
    ]
