# Generated by Django 3.0.1 on 2019-12-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paroll', '0002_auto_20191225_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='identity',
        ),
        migrations.AddField(
            model_name='paycheck',
            name='identity',
            field=models.CharField(default=0, max_length=4),
        ),
    ]