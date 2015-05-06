from django.conf.urls import patterns, url
from TodoLib import views

urlpatterns = patterns('',
	
	     url(r'^$', views.IndexView.as_view()),
		    url(r'^index$', views.IndexView.as_view()),
		  url(r'^create$', views.CreateView.as_view()),
	
   
)