# Generated by Django 3.2.5 on 2021-07-10 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registry',
            old_name='fieldName',
            new_name='date',
        ),
    ]