# Generated by Django 3.0.6 on 2020-05-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=15)),
                ('commissionRate', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]