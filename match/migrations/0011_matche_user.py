# Generated by Django 3.2.9 on 2022-09-28 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0010_matche_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='matche',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_match', to=settings.AUTH_USER_MODEL),
        ),
    ]