# Generated by Django 3.2.9 on 2021-11-13 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='name',
            field=models.CharField(default='null', max_length=150, verbose_name='Улица'),
        ),
    ]
