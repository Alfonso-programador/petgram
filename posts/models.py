from django.db import models
from users.models import User
import datetime
# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to='users/posts')
	description = models.TextField(blank = True)
	created = models.TextField()

class Likes(models.Model):
	id = models.AutoField(primary_key=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
	liked_by = models.IntegerField(null=True)