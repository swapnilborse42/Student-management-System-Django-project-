# Generated by Django 2.2.5 on 2019-09-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_auto_20190919_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
    ]