# Generated by Django 3.2.9 on 2022-09-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='awaylogo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='homeLogo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]