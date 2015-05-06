from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from TodoLib.models import Todo


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    model = Todo

	
class CreateView(CreateView):
	template_name = 'create.html'
	fields = ['name','description','deadline','progress']
	model = Todo

	
def contact(request):
	template = loader.get_template('contact.html')   
	return HttpResponse(template.render()) 
	
