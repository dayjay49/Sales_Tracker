# Generated by Django 3.0.6 on 2020-05-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesEntry', '0002_auto_20200514_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesentry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]