from django.conf.urls import patterns, url
from TodoLib import views

urlpatterns = patterns('',
	
	  
		 url(r'^$', views.index, name='index'), 
		 url(r'^create/$', views.CreateView.as_view(), name='create'),
		 url(r'^contact/$', views.contact, name='contact')
	
   
)