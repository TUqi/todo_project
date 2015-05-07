from django.conf.urls import patterns, url
from TodoLib import views

urlpatterns = patterns('',
	
	  
		 url(r'^$', views.IndexView.as_view(), name='index'), 
		 url(r'^create/$', views.CreateView.as_view(), name='create'),
		 url(r'^contact/$', views.contact, name='contact'),
		 url(r'^edit/(?P<pk>\d+)/$', views.EditView.as_view(), name ='edit'),
		 url(r'^delete/(?P<pk>\d+)/$', views.DeleteView.as_view(), name ='delete'),

		 
   
)
