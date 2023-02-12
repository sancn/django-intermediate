from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_django(request):
    return render(request, 'fees1.html')

def fees_Python(request):
    return render(request, 'fees2.html')
