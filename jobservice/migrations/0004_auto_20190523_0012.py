# Generated by Django 2.2 on 2019-05-22 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobservice', '0003_auto_20190522_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='postdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
