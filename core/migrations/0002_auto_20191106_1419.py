# Generated by Django 2.2.6 on 2019-11-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='graph',
            field=models.CharField(choices=[('NVIDIA', 'NVIDIA'), ('AMD', 'AMD')], default='NVIDIA', max_length=1),
        ),
        migrations.AlterField(
            model_name='proce',
            name='proce',
            field=models.CharField(choices=[('Intel', 'Intel'), ('AMD', 'AMD')], default='Intel', max_length=10),
        ),
    ]
