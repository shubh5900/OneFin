from django.urls import path
from . import views

urlpatterns = [
    path("Registration-1/",views.Registration),

    path("",views.Login),

    path("Login/",views.Login),

    path("Home/",views.Home),
]
