# Generated by Django 3.2 on 2022-02-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_spotless_app', '0002_alter_service_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='replied',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'In progress'), (2, 'Blocked'), (3, 'Done')], default=False),
        ),
    ]
