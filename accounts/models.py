from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  phone =  models.CharField(max_length=20 , default="")
  contry = models.CharField(max_length=100,default="")
  
 
  def __str__(self):
    return str(self.user)
  
@receiver(signal= post_save, sender= User)
def on_creat_user(sender ,instance,created ,**kwargs):
  if created:
    Profile.objects.create(user = instance)