from django.contrib import admin
from django.urls import path,re_path,include
from course import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    re_path("learndj/",views.learn_django),
    re_path("learnpy/",views.learn_Python),

]
