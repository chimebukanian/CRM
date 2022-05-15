from marketing.views import Homepage
from django.urls import path

urlpatterns=[
    path('', Homepage.as_view(), name="home"),

]