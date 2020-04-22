from django.urls import path, include
from user import views
from django.contrib.auth import urls

app_name = 'user'

urlpatterns = [
	path('register', views.RegisterView.as_view(), name = 'register'),
	# path('login/', views.LoginView.as_View(), name = 'login'),
	# path('logout/', views.LogoutView.as_View(), name = 'logout'),
	path('', include(urls)),
]
