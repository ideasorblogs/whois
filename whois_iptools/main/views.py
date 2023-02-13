from django.db.models import Count
from django.shortcuts import render
from django.views.generic import *
from whois_app.models import *

# Create your views here.


class index(ListView):
    model = SearchTerm
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        popular_domains = SearchTerm.objects.values('keywords').annotate(count=Count('keywords')).order_by('-count')[:3]
        return render(request, 'home/index.html', {'popular_domains': popular_domains})