from django.urls import path,re_path
from . import views
urlpatterns=[
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),

]
