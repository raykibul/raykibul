from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
    return render( index,'home.html')

def contact(index):
    return HttpResponse('This Is Contact page')

def about(index):
    return HttpResponse('This IS About Page')

