from django.contrib import admin
from django.urls import path
from .import views
from servis.views import ser
from kontak.views import kont

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kontak/', kont),
    path('servis/', ser),
    path('',views.bengkel),
]
