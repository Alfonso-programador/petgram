from django.shortcuts import render,redirect
from users.models import User,Followers
from .models import Post,Likes
import datetime
# Posts views
#Functions
def redirect_update(request):
	email = request.session['email']
	user = User.objects.get(email=email)
	if not user.picture or not user.biography:
		print("no hay")
		return True
	else:
		print("hay")
		return False

#Other Profiles
def profile(request,email):
	if 'email' in request.session:
		actual_email = request.session['email']
		if email == actual_email:
			return redirect("users:profile")
		user =  User.objects.get(email=email)
		me =  User.objects.get(email=actual_email)
		posts = Post.objects.filter(user_id=user)
		if actual_email == user.email:
			is_me = True
		else:
			is_me = False

		if request.method == "POST":
			follow = Followers()
			follow.user_id = user.id
			follow.followed_by = me.id
			follow.save()

		followed = Followers.objects.filter(followed_by = me.id)
		followers = Followers.objects.filter(user_id=me.id)
	return render(request,"app/other_profile.html",context={
		"user":user,
		"posts":posts,
		"is_me":is_me,
		"followed":followed,
		"followers" : followers
		})

#Views



def feed(request):
	if request.method == "POST":
		email = request.session['email']
		user = User.objects.get(email=email)
		post_id = request.POST["like"]
		likes = Likes()
		likes.post_id = post_id
		likes.liked_by = user.id
		likes.save()

	date = datetime.datetime.now()
	current_date = date.strftime("%B %d")
	if 'email' in request.session:
		email = request.session['email']
		redirect_val = redirect_update(request)	
		if redirect_val:
			return redirect('posts:update_profile')
		else:
			current_user = request.session['email']
			me =  User.objects.get(email=current_user)
			try:
				follow = Followers.objects.get(followed_by=me.id)
				posts = Post.objects.filter(user_id=follow.user_id,created=current_date)
				other_user = User.objects.get(id=follow.user_id)
				context = {
					'current_user':current_user,
					"posts":posts,
					"other_user":other_user,
					"current_date":current_date,
			}
			except Followers.DoesNotExist:
				print("No existe")
				context = {}
			
			return render(request,'app/feed.html',context)
	else:
		return redirect('users:login')

	


def newPost(request):
	date = datetime.datetime.now()
	if "email" in request.session:
		email = request.session['email']
		posts = Post()
		user = User.objects.get(email=email)
		if request.method == "POST":
			posts.image = request.FILES["image"]
			posts.description = request.POST['description']
			posts.user_id =  user.id
			posts.created = date.strftime("%B %d")
			posts.save()
			return redirect("posts:feed")
		
	return render(request,'app/new_post.html')



def update(request):
	email = request.session['email']
	user = User.objects.get(email=email)
	if request.method == "POST":
		user.picture = request.FILES["picture"]
		user.biography = request.POST["biography"]
		user.phone_number = request.POST["phone"]
		user.save()

	return render(request,'users/update_profile.html',user.__dict__,)