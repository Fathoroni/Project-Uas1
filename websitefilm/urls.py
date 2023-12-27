from django.contrib import admin
from django.urls import include,path
from nontonkuy.views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

]
