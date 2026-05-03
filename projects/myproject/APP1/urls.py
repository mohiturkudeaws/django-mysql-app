from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
     path('application',views.application,name="application"),
      path('login',views.login,name="login")
]