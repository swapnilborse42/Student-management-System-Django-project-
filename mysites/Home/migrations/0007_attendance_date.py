# Generated by Django 2.2.5 on 2019-09-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
