# Generated by Django 2.2.5 on 2019-09-14 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20190914_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
