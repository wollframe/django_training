
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from samplesite import settings
from .views import *


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('detail/<int:bb_id>/', detail, name='detail'),
    path('',index,  name='index'),
]
