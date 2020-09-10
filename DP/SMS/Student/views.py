from django.shortcuts import render
from django.http import HttpResponse
from .models import Stud
# Create your views here.

dd ={
'name' :Stud.objects.all()

}
def home(request):
    return render(request,'Student/home.html',dd)
    #return HttpResponse("<h1> Home Page </h1>")
def about(request):
    return HttpResponse("<h1> About Page </h1>")
