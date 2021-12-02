from django.urls import path
from users import views


urlpatterns = [
	path('login/',views.login,name = "login"),
	path('logout/',views.logout,name = "logout"),
	path('signup/',views.signup,name = "signup"),
	path('me/',views.profile,name='profile'),
	path('search/',views.search_results,name="search")
]