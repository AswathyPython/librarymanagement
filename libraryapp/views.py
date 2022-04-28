from django.shortcuts import render
from.models import *

# Create your views here.
def home(request):
    prod=books.objects.all()
    return render(request,'index.html',{'pr':prod})