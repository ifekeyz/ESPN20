from django.contrib import admin

# Register your models here.
from .models import Matche,Market,BetOdd


admin.site.register(Matche)
admin.site.register(Market)
admin.site.register(BetOdd)