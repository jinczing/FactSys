# Generated by Django 3.0.1 on 2019-12-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=4)),
                ('password', models.CharField(default='00000', max_length=200)),
                ('work_duration', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('account_type', models.CharField(max_length=200)),
                ('bank_account', models.IntegerField(default=0)),
                ('email', models.EmailField(default='none', max_length=254)),
                ('commission', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('taxes', models.IntegerField(default=0)),
                ('health_insurance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=4)),
                ('work_state', models.CharField(max_length=200)),
                ('work_shift', models.CharField(max_length=200)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paroll.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='date applied')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paroll.Account')),
            ],
        ),
    ]
