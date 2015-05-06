from django.views.generic import CreateView, UpdateView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from TodoLib.models import Todo


# Create your views here.
def index(request):
	template = loader.get_template('index.html')   
	todos=Todo.objects.all()
	context=RequestContext(request, {'todos':todos,})
	return HttpResponse(template.render(context)) 

	
class CreateView(CreateView):
	template_name = 'create.html'
	fields = ['name','description','deadline','progress']
	model = Todo
	
#class EditView(UpdateView):
	#template_name = 'edit.html'
   # fields = ('title','description', 'deadline', 'progress',)
   # model = Todo

	
def contact(request):
	template = loader.get_template('contact.html')   
	return HttpResponse(template.render()) 
	
