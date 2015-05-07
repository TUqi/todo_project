from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from TodoLib.models import Todo



class IndexView(ListView):
    template_name = 'index.html'
    model = Todo

	
class CreateView(CreateView):
	template_name = 'create.html'
	fields = ['name','description','deadline','progress']
	model = Todo
	success_url = '/todo'
	
	
class EditView(UpdateView):
	template_name = 'edit.html'
	fields = ['name','description','deadline','progress']
	model = Todo
	success_url = '/todo'
	
class DeleteView(DeleteView):
	model = Todo
	success_url = '/todo'
	
	
	
	

def contact(request):
	template = loader.get_template('contact.html')   
	return HttpResponse(template.render()) 
	
