# Generated by Django 3.0.6 on 2020-05-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(choices=[('FLL', 'Fresh Lemon Lemonade'), ('OLS', 'Orange & Lemon Splash'), ('SS', 'Sugary Shocker'), ('WWW', 'Wild Whiskey Whack')], default='FLL', max_length=50)),
                ('staffName', models.CharField(choices=[('JT', 'Jeff Terry'), ('TB', 'Thomas Black'), ('JR', 'John Rice'), ('LL', 'Larry Long')], default='TB', max_length=40)),
                ('date', models.DateField(auto_now_add=True)),
                ('numOfCups', models.PositiveSmallIntegerField()),
            ],
        ),
    ]