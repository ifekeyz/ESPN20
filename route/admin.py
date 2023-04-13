from django.contrib import admin


# Register your models here.
from .models import invitationCode,Recharge,CustomUser,Withdrawal,Betting,ForgotPswd

class BettingAdmin(admin.ModelAdmin):
    list_display = ('match','scores','amount','username')
    list_display_links = ('match','username')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email','amount','username')
    list_display_links = ('id','username')

class RechargeAdmin(admin.ModelAdmin):
    list_display = ('id','name','confirm')
    list_display_links = ('id','name')

class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('id','username','chain','amountToWithdraw','confirm')
    list_display_links = ('id','username')

admin.site.register(invitationCode)
admin.site.register(Recharge,RechargeAdmin)
admin.site.register(Withdrawal,WithdrawalAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Betting,BettingAdmin)
admin.site.register(ForgotPswd)
