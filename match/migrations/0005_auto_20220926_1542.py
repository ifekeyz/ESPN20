# Generated by Django 3.2.9 on 2022-09-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_auto_20220926_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='awayGoal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='awaylogo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='market',
            name='homeGoal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='homeLogo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]