# Generated by Django 3.2 on 2022-02-25 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_spotless_app', '0003_auto_20220225_1010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Upcoming',
            new_name='Booking',
        ),
    ]