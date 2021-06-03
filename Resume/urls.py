from django.urls import path

from . import views



urlpatterns = [
	path('', views.index, name = 'index'),
	path('addnew/', views.addnew, name = 'addnew'),
	path('<int:resume_id>/', views.resume_details, name='resume_details'),
	path('<int:resume_id>/edit/', views.editresume, name="editresume"),
	path('<int:resume_id>/delete/', views.deleteresume, name="deleteresume"),	
	path('login/', views.login, name = 'login'),
	path('logout/', views.logout, name = 'logout'),
	path('signup/', views.signup, name = 'signup'),
	path('<int:resume_id>/download/', views.download, name = 'download'),
]	
