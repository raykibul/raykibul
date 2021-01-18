from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(index):
    return render( index,'home/home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['inputName']
        email=request.POST['inputEmail']
        message=request.POST['message']
        contact=Contact(name=name,email=email,message=message)
        if len(name)<2 or len(email)<3 or len(message)<4:
            messages.error(request,"Please Fill the Form Correctly!!")
        else:
            messages.success(request,"Thank You !! Your Message has been sent!")
            contact.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

