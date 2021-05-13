
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="Home-page"),
    path('database/', views.database_view, name="Database-page"),
]

