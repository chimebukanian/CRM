from django.urls import path
from .views import new_suscriber
urlpatterns=[
    path('', new_suscriber, name="signup"),

]