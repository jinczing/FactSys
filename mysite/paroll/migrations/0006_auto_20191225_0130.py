# Generated by Django 3.0.1 on 2019-12-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paroll', '0005_auto_20191225_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default=0, max_length=200000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_account',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='paycheck',
            name='deduction',
            field=models.CharField(max_length=200000),
        ),
        migrations.AlterField(
            model_name='paycheck',
            name='salary',
            field=models.CharField(max_length=2000000),
        ),
    ]