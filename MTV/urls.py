from django.urls import path
from MTV import views

app_name = 'MTV'
urlpatterns = [
  path('',views.index),
 
]