# Generated by Django 2.2.5 on 2019-09-19 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20190919_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='subject',
            new_name='subject_name',
        ),
    ]