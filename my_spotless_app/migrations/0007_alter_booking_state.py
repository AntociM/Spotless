# Generated by Django 3.2 on 2022-03-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_spotless_app', '0006_alter_booking_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.IntegerField(choices=[(0, 'WAITING'), (1, 'APPROVED'), (1, 'IN PROGRESS'), (2, 'BLOCKED'), (3, 'DONE')], default=False),
        ),
    ]
