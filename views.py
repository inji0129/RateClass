#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Start
from django.db.models import Q

class start(TemplateView):
    template_name='rate/start.html'

class Search(ListView):
    model = Start
    template_name='rate/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Start.objects.filter(
            Q(class_name__icontains=query) | Q(prof_name__icontains=query))

        return object_list

# Create your views here.
