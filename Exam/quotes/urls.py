from django.urls import path
from . import views

urlpatterns=[
                path('', views.home, name="home"),
                path('about.html', views.about, name="about"),
                path('optimal.html', views.optimal, name="optimal"),
                path('stockticks.html',views.stockticks,name="stockticks")
    ]