from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    cname='django'
    duration='4months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    coursename={'cname':'jinja2'}
    return render(request,'course/course1.html',context=django_details)

#########################
def learn_python(request):
    return render(request,'course/course2.html')
