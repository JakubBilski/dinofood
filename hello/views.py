from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
     return HttpResponse('Hello Karol, Kuba, Kuba!')
    #return render(request, "index.html")



