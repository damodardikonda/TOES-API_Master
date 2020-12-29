from django.shortcuts import render
from authapp.models import Worker_Details, Job_Details, User, Categories
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from authapp.serializers import *
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parseres import JSONParser
import requests
import json
# from authapp impo

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_job(request , user ):
    cursor = connection.cursor()
    # take 3 catagories of workers
    cursor.execute('select catagory_1 , category_2 ,category_3  from authapp_worker_details where user_id = user')
    row = cursor.fetchall()

    cursor.execute('select name ,job_title from authapp_user INNER JOIN authapp_job_details on authapp_user.id = authapp_job_details.recruter_id')
    row1 = cursor.fetchall()
    content = {}
    payload = []
    for res in row:
        for res1 in row1:
           if res[0] == res1[1] or res[1] == res1[1] or res[2] == res1[1]:
               content = {
                          'recruter_name' : res1[0],
                          'category_1': res1[1],


                         }
               payload.append(content)


    return Response(data=payload, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_recruter_job(request , recruterid):
    cursor = connection.cursor()

     #take name , adress , title discription and amount from databases


     cursor.execute('select name,recruter_id,address , job_Description  from authapp_user INNER JOIN authapp_job_details on authapp_user.id = authapp_job_details.recruter_id ')
     row = cursor.fetchall()
     content = {}
     payload = []
     for result in row:
         if recruterid == result[1]:
             content = {

                       'name' : result[0],
                       'address' : result[2],
                       'job_Description' : result[3],
                       'amount': result[4],
             }
             payload.append(content)
     return Response(data = payload , status = status.HTTP_200_OK)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def display_to_recruter(request , recruterid ,workerid , catagory):
    '''cursor = connection.cursor()
    cursor.execute(select worker_id ,recruter_id, name ,city ,job_Description ,catagory_1, category_1_vc , catagory_2 , category_2_vc ,catagory_3, category_3_vc from authapp_user INNER JOIN authapp_worker_details using(user) INNER JOIN authapp_job_details on authapp_user.user = authapp_job_details.recruter_id)
    row = cursor.fetchall()

    content = {}
    payload = []
    for result in row:
        if recruterid = result[1] and  category = result[5]:
            content ={

                      'name' : 'name',
                      'city' : 'city',
                      'job_Description' :'job_Description',
                      'category_1_vc' : 'catagory_1_vc'
             }
        elif recruterid = result[1] and  category = result[7]:
             content ={

                   'name' : 'name',
                   'city' : 'city',
                   'job_Description' :'job_Description',
                   'category_2_vc' : 'catagory_2_vc'
               }
        elif recruterid = result[1] and  category = result[9]:
              content ={

                        'name' : 'name',
                        'city' : 'city',
                        'job_Description' :'job_Description',
                        'category_3_vc' : 'catagory_3_vc'
              }

        payload.append(content)
      '''
      if request.method = 'GET':
          json_data = requests.body
          stream = io.ByteIO(json_data)
          pythondata = JSONParser().parse(stream)
          id = pythondata.get_id('recruiter_name')


#Finding out username by using recruiters id
@api_view(['get'])
@permission_classes([IsAuthenticated])
def disp_workertorecruiter(request):

        if request.method == GET :

            #it will load all request data into Json data
            json_data = request.body

            stream = io.ByteIO(json_data)

            #converting json data into python data
            pythondata = JSONParser().parse(stream)

            #taking myapp.py id into this id
            id = pythondata.get('id' , None)

            # taking myapp.py-worker_id from id  into worker_id
            worker_id = id[worker_id]
            recruiter_name = id[recruiter_name]


            cursor = connection.cursor()

            #take recruiters id
            cursor.execute(select  recruiter_id  from authapp_user INNER JOIN authapp_job_details where authapp_user.name = recruiter_name )
            row = cursor.fetchall()

            #taker workers detail
            cursor.execute( select name , city , job_Description , amount from authapp_user INNER JOIN authapp.Worker_Details using(user) INNER JOIN authapp_job_details on authapp_job_details.recruter_id = worker_id )
            row1 = cursor.fetchall()



            content = {}
            payload = []
            for result in row:
                for res in row1:
                   if recruterid = result[0] :
                         content ={

                                  'name' : res[0],
                                  'city' : res[1],
                                  'job_Description' :res[2],
                                  'amount' : res[3]
                         }
            payload.append(content)
    return Response(data=payload, status=status.HTTP_200_OK)

    
