from django.urls import path
from posts import views

urlpatterns = [
	path('',views.feed,name="feed"),
	path('new',views.newPost,name="new"),
	path('update_profile',views.update,name="update_profile"),
	path('p/<str:email>',views.profile,name='others_profile'),
]