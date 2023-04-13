
from django.db import models
# import random
# Create your models here.
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from datetime import datetime


# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)

from django.contrib.auth.models import AbstractUser
from requests import request

class CustomUser(AbstractUser):
    amount = models.CharField(max_length=100,default=0, null=True,blank=True)
    legal = models.CharField(max_length=200,null=True,blank=T)
    # phoneNo = models.CharField(max_length=30,blank=True, null=True)
    # if your additional field is a required field, just add it, don't forget to add 'email' field too.
    # REQUIRED_FIELDS = ['mobile', 'email']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


    def balance_account(self):


        balance = CustomUser.objects.get(amount=request.user.amount)
        
        exact_balance = []


        for profile in balance:
            if profile.account == self.user:
                exact_balance.reverse(profile)
        return exact_balance

            



class invitationCode(models.Model):
    code = models.CharField(max_length=100)
    

    def __str__(self):
        return self.code


class Withdrawal(models.Model):
    username = models.CharField(max_length=50,blank=True)
    amountToWithdraw = models.CharField(max_length=50,null=True,blank=True)
    amountbalance = models.CharField(max_length=50,null=True,blank=True)
    chain = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=50,blank=True)
    confirm = models.BooleanField(default=False)


    def __str__(self):
        return self.username





class Recharge(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    transactionid = models.CharField(max_length=200, blank=True)
    chain = models.CharField(max_length=20,blank=True)
    amount = models.CharField(max_length=200, blank=True)
    paymentProve = models.ImageField(upload_to='images/', blank=True, null=True)
    confirm = models.BooleanField(default="False")

    def __str__(self):
        return self.name

class Betting(models.Model):
    username = models.CharField(max_length=200, blank=True)
    amount = models.CharField(max_length=200, blank=True)
    listingDate = models.DateTimeField(default = datetime.now, blank=True,editable=True)
    match = models.CharField(max_length=200, blank=True)
    SCORE = (('1 - 0','1 - 0'),("2 - 0","2 - 0"),("3 - 0","3 - 0"),("0 - 1","0 - 1"),("0 - 2","0 - 2"),("0 - 3","0 - 3")
    ,("1 - 1","1 - 1"),("1 - 2","1 - 2"),("1 - 3","1 - 3"),("2 - 1","2 - 1"),("2 - 2","2 - 2"),("2 - 3","2 - 3"),("3 - 1","3 - 1")
    ,("3 - 2","3 - 2"),("3 - 3","3 - 3"),("4 - 3","4 - 3"))
    scores = models.CharField(max_length=200, blank=True, null=True,editable=True)
    profit = models.CharField(max_length=200, blank=True, null=True,editable=True)
    OPTION = (("Pending","Pending"),("Success","Success"))
    status = models.CharField(choices=OPTION, max_length=10, default="Pending")
    won = models.BooleanField(default=False, )

    def __str__(self):
        return self.username

    


class ForgotPswd(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    forgetpasswordtoken = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username