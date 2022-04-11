#users/urls.py

from django.urls import path
from . import views
urlpatterns = [

 path('', views.home, name = "home"),
 path("signup/", views.SignUp.as_view(), name="signup"),
 path("search/", views.TickerSearch.as_view(), name = "ttcksearch"),
 path('search/results/', views.Analysis, name="tickersymbolanalysis"),
]