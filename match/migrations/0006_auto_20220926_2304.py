# Generated by Django 3.2.9 on 2022-09-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20220926_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='leagueLogo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='leagueSeason',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
