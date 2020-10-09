

from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name = "home"),
    path('count/',views.count,name = "count"),# name value has to be the same as the the form action value on the home.html page
    path('about/',views.about, name = "about")
]
