# Generated by Django 2.2.24 on 2021-07-14 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210714_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registry',
            old_name='default_field',
            new_name='key',
        ),
        migrations.AddField(
            model_name='registry',
            name='passsword',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 14, 18, 37, 55, 313378)),
        ),
    ]
