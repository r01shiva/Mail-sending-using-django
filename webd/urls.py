from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

	path('',views.main,name='main'),
    url(r'^applicants/$',views.IndexViewPro.as_view(),name='applicants'),
]
