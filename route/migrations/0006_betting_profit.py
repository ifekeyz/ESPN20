# Generated by Django 3.2.9 on 2022-10-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0005_alter_recharge_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='betting',
            name='profit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
