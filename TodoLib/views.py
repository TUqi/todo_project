from django.views.generic import TemplateView
from django.views.generic import CreateView
from TodoLib.models import Todo

# Create your views here.
class IndexView(Template):
    template_name = 'index.html'
    model = Todo

class CreateView(CreateView):
	template_name = 'create.html'
	model = Todo
	success_url = '/'	

