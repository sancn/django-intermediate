from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fees_django(request):
    return HttpResponse('Pay your fees for django course')