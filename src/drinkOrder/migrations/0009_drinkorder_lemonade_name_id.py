# Generated by Django 3.0.6 on 2020-05-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkOrder', '0008_auto_20200517_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinkorder',
            name='lemonade_name_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
