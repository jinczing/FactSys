# Generated by Django 3.0.1 on 2019-12-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShiftMana', '0002_auto_20191223_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulestate',
            name='work_shift',
            field=models.CharField(default='morning', max_length=200),
        ),
        migrations.AlterField(
            model_name='schedulestate',
            name='work_state',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
