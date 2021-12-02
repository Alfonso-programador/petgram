from django.db import models
class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30,unique=True)
	password = models.CharField(max_length=30)
	picture = models.ImageField(upload_to='users/pictures',blank = True,default=None)
	biography = models.TextField(blank = True,default = None)
	phone_number = models.CharField(max_length=20,blank = True)
	

	def __str__(self): #Instancia de este modelo
		return self.first_name
	

class Followers(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	followed_by = models.IntegerField(null=True)