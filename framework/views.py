from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import responses
from rest_framework.decorators import api_view
from .models import employee
from .serializer import employeeserielizer

# Create your views here.

class employeelist(APIView):
    def get(self,request):
        employee1 = employee.objects.all()
        serilezer  =employeeserielizer(employee1,many = True)
        return responses(serilezer.data)
    def post(self):
        pass