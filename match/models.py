from django.db import models

from route.models import CustomUser


# Create your models here.
class Matche(models.Model):
    league = models.CharField(max_length=100,blank=True)
    leagueLogo = models.CharField(max_length=100,blank=True,null=True)
    leagueSeason = models.CharField(max_length=100,blank=True,null=True)
    home = models.CharField(max_length=100,blank=True)
    away = models.CharField(max_length=100,blank=True)
    homeGoal = models.CharField(max_length=100,blank=True, null=True)
    finalscores = models.CharField(max_length=100,blank=True, null=True)
    awayGoal = models.CharField(max_length=100,blank=True,null=True)
    homeLogo = models.CharField(max_length=100,blank=True)
    awaylogo = models.CharField(max_length=100,blank=True)
    matchTime = models.CharField(max_length=100,blank=True)
    SCORE = (('1 - 0','1 - 0'),("2 - 0","2 - 0"),("3 - 0","3 - 0"),("0 - 1","0 - 1"),("0 - 2","0 - 2"),("0 - 3","0 - 3")
    ,("1 - 1","1 - 1"),("1 - 2","1 - 2"),("1 - 3","1 - 3"),("2 - 1","2 - 1"),("2 - 2","2 - 2"),("2 - 3","2 - 3"),("3 - 1","3 - 1")
    ,("3 - 2","3 - 2"),("3 - 3","3 - 3"),("4 - 3","4 - 3"))
    scores = models.CharField(choices=SCORE, max_length=200, blank=True, null=True)
    user = models.OneToOneField(CustomUser, related_name='user_match',on_delete=models.CASCADE,blank=True,null=True)
    bet1 = models.CharField(max_length=100,blank=True,default="1 - 0")
    bet2 = models.CharField(max_length=100,blank=True,default="2 - 0")
    bet3 = models.CharField(max_length=100,blank=True,default="3 - 0")
    bet4 = models.CharField(max_length=100,blank=True,default="0 - 1")
    bet5 = models.CharField(max_length=100,blank=True,default="0 - 2")
    bet6 = models.CharField(max_length=100,blank=True,default="0 - 3")
    bet7 = models.CharField(max_length=100,blank=True,default="1 - 1")
    bet8 = models.CharField(max_length=100,blank=True,default="1 - 2")
    bet9 = models.CharField(max_length=100,blank=True,default="1 - 3")
    bet10 = models.CharField(max_length=100,blank=True,default="2 - 1")
    bet11 = models.CharField(max_length=100,blank=True,default="2 - 2")
    bet12 = models.CharField(max_length=100,blank=True,default="2 - 3")
    bet13 = models.CharField(max_length=100,blank=True,default="3 - 1")
    bet14 = models.CharField(max_length=100,blank=True,default="3 - 2")
    bet15 = models.CharField(max_length=100,blank=True,default="3 - 3")
    bet16 = models.CharField(max_length=100,blank=True,default="4 - 3",null=True)
    odds1 = models.CharField(max_length=100,blank=True,default="3.92")
    odds2 = models.CharField(max_length=100,blank=True,default="7.12")
    odds3 = models.CharField(max_length=100,blank=True,default="0.65")
    odds4 = models.CharField(max_length=100,blank=True,default="3.57")
    odds5 = models.CharField(max_length=100,blank=True,default="1.05")
    odds6 = models.CharField(max_length=100,blank=True,default="2.12")
    odds7 = models.CharField(max_length=100,blank=True,default="7.18")
    odds8 = models.CharField(max_length=100,blank=True,default="1.53")
    odds9 = models.CharField(max_length=100,blank=True,default="0.03")
    odds10 = models.CharField(max_length=100,blank=True,default="3.11")
    odds11 = models.CharField(max_length=100,blank=True,default="3.38")
    odds12 = models.CharField(max_length=100,blank=True,default="0.93")
    odds13 = models.CharField(max_length=100,blank=True,default="3.91")
    odds14 = models.CharField(max_length=100,blank=True,default="5.87")
    odds15 = models.CharField(max_length=100,blank=True,default="7.61")
    odds16 = models.CharField(max_length=100,blank=True,default="2.03",null=True)


    def __str__(self):
        return f"{self.league} -------> {self.home} vs {self.away}"

    def profit(self):
        pass



class Market(models.Model):
    league = models.CharField(max_length=100,blank=True)
    home = models.CharField(max_length=100,blank=True)
    away = models.CharField(max_length=100,blank=True)
    homeGoal = models.CharField(max_length=100,blank=True,null=True)
    awayGoal = models.CharField(max_length=100,blank=True,null=True)
    homeLogo = models.CharField(max_length=100,blank=True)
    awaylogo = models.CharField(max_length=100,blank=True)
    matchTime = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return f"{self.league} -------> {self.home} vs {self.away}"



class BetOdd(models.Model):
    
    scores = models.CharField(max_length=100,blank=True)
    odds = models.CharField(max_length=100,blank=True)
   

    def __str__(self):
        return self.scores