from django.db import models

# Create your models here.
from route.models import CustomUser
from .utils import generate_ref_code





class Profile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='user_profile',on_delete=models.CASCADE)
    code = models.CharField(max_length=12,blank=True)
    recommended_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True,null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.code}"

    def get_recommened_profiles(self):
        qs = Profile.objects.all()
        # my_resc = [p for p in qs if p.recommended_by == self.user]

        my_resc = []

        for profile in qs:
            if profile.recommended_by == self.user:
                my_resc.append(profile)
        return my_resc

  
    def save(self, *args, **kwargs):

        if self.code == "":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)

class Betting_History(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    match_ids = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.user_id.username