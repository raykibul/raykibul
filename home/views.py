from django.shortcuts import render
from django.template.response import HttpResponse
from django.views.decorators.http import require_http_methods


# Create your views here.


@require_http_methods(["GET"])
def home_page(request):
    return HttpResponse("Hello there")
