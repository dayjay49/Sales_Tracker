# Generated by Django 3.0.6 on 2020-05-14 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesEntry', '0003_auto_20200514_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesentry',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
