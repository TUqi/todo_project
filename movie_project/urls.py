from django.conf.urls import include, url
from django.contrib import admin
from TodoLib import urls
from TodoLib import views


urlpatterns = [

 url(r'^todo/', include('TodoLib.urls', namespace='todo')),
    url(r'^admin/', include(admin.site.urls)),

    


    	 


]
