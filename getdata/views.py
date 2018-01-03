from django.shortcuts import render
from .forms import DataForm
from .models import DataPoint
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import django

# Create your views here.
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DataForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #ImageData = form.cleaned_data["draw_image"]
            point = form.save()
            #point.time =  # save time here
            #point.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DataForm()
    data = DataPoint.objects.all()
    version = django.get_version()
    return render(request, 'getdata/index.html', {'form': form,'version': version,'data': data})