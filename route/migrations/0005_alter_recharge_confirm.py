# Generated by Django 3.2.9 on 2022-10-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_recharge_chain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='confirm',
            field=models.BooleanField(default='False'),
        ),
    ]
