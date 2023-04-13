from django.contrib import admin

# Register your models here.
from .models import Profile,Betting_History


admin.site.register(Profile)
admin.site.register(Betting_History)