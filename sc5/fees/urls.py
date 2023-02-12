from django.urls import path,re_path
from . import views
urlpatterns=[
    path('feesdj/',views.fees_django),
    path('feespy/',views.fees_python),

]
