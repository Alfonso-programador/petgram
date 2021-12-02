from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User,Followers
from .forms import UserForm
from posts.models import Post
from django.db.models import Count
# Users views

#For images media
#Function
def search_results(request):
	if request.is_ajax():
		email = request.session['email']
		res = None
		user = request.POST.get('user')
		users_search = User.objects.filter(first_name__icontains=user)
		if len(user) > 0 and len(users_search)>0:
			data = []
			for position in users_search:
				item = {
					'username': position.username,
					'first_name':position.first_name,
					'last_name':position.last_name,
					'email':position.email,
					'picture':str(position.picture.url)

				}
				data.append(item)
			res = data
		else:
			res = 'No users found'

		return JsonResponse({'data':res})
	
	return JsonResponse({})
#Views
def login(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		check_user = User.objects.filter(email=email,password = password)
		if check_user:
			request.session['email'] = email
			return redirect('posts:feed') 
		else:
			return redirect("users:login")
	return render(request,'users/login.html')


def signup(request):
		if request.method == 'POST':
		
			form = UserForm()
			form = UserForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('users:login')
		else:
			form = UserForm()


		return render(request,'users/signup.html',{
				'form':form
			})
	
def logout(request):
	try:
		del request.session['email']
	except:
		return redirect('users:login')

	return redirect("users:login")

	
def profile(request):
	email = request.session['email']
	user = User.objects.get(email=email)
	posts = Post.objects.filter(user_id=user)
	followers = Followers.objects.filter(user_id=user.id)
	follow = Followers.objects.filter(followed_by=user.id)

	return render(request,'users/profile.html',context={
		"user":user,
		"posts":posts,
		"followers":followers,
		"follow": follow
		})