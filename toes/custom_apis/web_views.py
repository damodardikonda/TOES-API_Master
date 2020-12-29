from django.shortcuts import render
from authapp.models import (
    WorkerDetails, JobDetails, User, Categories
    )
from authapp.models import WorkerDetails, JobDetails, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
import json

from authapp.serializers import UserCreateSerializer


# for displaying total workers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_total_wokers(request):
    '''cursor = connection.cursor()

    cursor.execute(' select COUNT(*)user_id from  authapp_workerdetails')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
    '''
    total_workers = authapp_workerdetails.objects.exclude(user_id = None).count()
    content = {

            'total_workers' : total_workers
    }

    #payload.append(content)


    return Response(content, status = status.HTTP_200_OK)



#For displaying total jobs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_total_jobs(request):
    '''cursor = connection.cursor()

    cursor.execute(' select COUNT(*)user_id from  authapp_workerdetails')
    row = cursor.fetchall()
    content = {}
    payload = []
    for data in row:
    '''
    total_jobs = jobdetails.objects.exclude(id = None).count()
    content = {

            'total_jobs' : total_jobs
    }

    #payload.append(content)


    return Response(content, status = status.HTTP_200_OK)


#for displaying total requests send by Recruiters
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_total_req(request):
    cursor = connection.cursor()
    cursor.execute(' select COUNT(*)id from  authapp_workersrequests')
    row = cursor.fetchall()

    cursor.execute('select COUNT(*)id from authapp_recruitersrequests')
    row1 = cursor.fetchall()


    content = {}
    payload = []
    for data in row:
       for data2 in row1:
           data3 = data[0] + data2[0]
    #total_jobs = jobdetails.objects.exclude(id = None).count()
           content = {

                'total_req' : data
           }

           payload.append(content)


    return Response(data = payload, status = status.HTTP_200_OK)



# for Total Accepted request which is accepted by Workers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home_accept_req(request):
     cursor = connection.cursor()
     cursor.execute(' select COUNT(*)id from  authapp_workersrequests where authapp_workersrequests.status = 1')
     row = cursor.fetchall()

     cursor.execute(' select COUNT(*)id from  authapp_recruitersrequests where authapp_recruitersrequests.status = 1')
     row1 = cursor.fetchall()

     content = {}
     payload = []
     for data in row:
        for data1 in row1:
            data2 = data[0] + data1[0]
     #total_jobs = jobdetails.objects.exclude(id = None).count()
            content = {

                 'total_req' : data
            }

            payload.append(content)


     return Response(data = payload, status = status.HTTP_200_OK)



#Registeration for thoes who doesnt have an smartphones
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def home_smart_reg(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        aadhar_no = request.POST.get('aadhar_no')
        work = request.POST.get('work')

        data = {

           'name' : name,
           'age':age,
           'phone':phone,
           'gender':gender,
           'address':address,
           'permanent_address': permanent_address,
           'aadhar_no':aadhar_no,
           'work':work,
           'smartphone':'0',
        }
        create_user_api = 'http://127.0.0.1:8000/smartreg'

        requests.post(create_user_api , json = data)
        return Response(data)
