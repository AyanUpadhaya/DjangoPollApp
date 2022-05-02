# main urls py file
from django.contrib import admin
from django.urls import path, include
from pollapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pollapp.urls'))
]
