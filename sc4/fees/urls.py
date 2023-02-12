from django.contrib import admin
from django.urls import path,re_path,include
from fees import views
urlpatterns = [
    # path("admin/", admin.site.urls),
    re_path("feesdj/",views.fees_django),
    re_path("feespy/",views.fees_Python),

]
