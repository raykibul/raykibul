from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('BLOG HOME')

def blogPost(request,slug):
    return HttpResponse('BLog Post: '+slug)
