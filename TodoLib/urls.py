from django.conf.urls import patterns, url
from TodoLib import views

urlpatterns = patterns('',
	# url(r'^$', views.CreateView.as_view()), #new line
	     url(r'^$', views.IndexView.as_view()),
	
   
)