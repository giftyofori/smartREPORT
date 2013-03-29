from django.db import models
from django.contrib import admin
from django.contrib.auth.signals import user_logged_in,  user_logged_out
from django.contrib import admin

from django.contrib.auth.models import User
from django.db.models.signals import post_save
class UserProfile(models.Model):
	picture = models.ImageField("Profile Pictue" , upload_to ="data/pro_images/", blank = True , null = True)
	logins = models.IntegerField(default = 0)
	user = models.ForeignKey(User , unique = True)
	
	def __unicode__(self):
		return self.user
		
def create_user_profile(sender , **kwargs):
# when creating a new user make a profile for him/ her
	u = kwargs['instance']
	if not UserProfile.objects.filter(user = u):
		UserProfile(user = u).save()

class LoggedUser(models.Model):
	username = models.CharField(max_length = 30 , primary_key = True)
	
	def __unicode__(self):
		return self.username

def login_user(sender , request , user , **kwargs):
	LoggedUser(username = user.username).save()

def logout_user(sender, request , user , **kwargs):
	try:
		u = LoggedUser.objects.get(pk = user.username)
		u.delete()
	except LoggedUser.DoesNotExist or Error:
		pass
	
user_logged_in.connect(login_user)
user_logged_out.connect(logout_user)
	


post_save.connect(create_user_profile , sender = User)
		
		

admin.site.register(LoggedUser)
