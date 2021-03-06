# Generated by Django 3.2.5 on 2021-07-12 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20210712_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 12, 20, 36, 22, 403453)),
        ),
        migrations.AlterField(
            model_name='registry',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
