from django.urls import path, include
from table import views

urlpatterns = [
    path("", views.homepage),
    path('leaguetable', views.tableview),
    path('pinnaclehighlight', views.pinnacleview),
]