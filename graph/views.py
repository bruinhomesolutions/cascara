from django.shortcuts import render
from getdata.forms import DataForm
from getdata.models import DataPoint
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import django

from django.http import JsonResponse

# Create your views here.

def graph(request):
    return render(request, 'graph/graph.html')

def value_over_time(request):
    data = DataPoint.objects.all().values('time','data').order_by('time')
    return JsonResponse(list(data), safe=False)