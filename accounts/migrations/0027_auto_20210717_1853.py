# Generated by Django 2.2.24 on 2021-07-17 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20210717_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 18, 53, 39, 192280)),
        ),
        migrations.AlterField(
            model_name='save_mail',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
