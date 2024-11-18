from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomeItemViews.as_view(), name='home')
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
