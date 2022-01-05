
from django.urls import path,include
from .views import employeelist
urlpatterns = [
   
    path('',employeelist.as_view()),
]
