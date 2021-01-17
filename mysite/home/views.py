from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
    return render( index,'home/home.html')

def contact(index):
    return render(index,'home/contact.html')

def about(index):
    return render(index,'home/about.html')

