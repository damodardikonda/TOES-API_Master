from django.shortcuts import render,redirect
from authapp.models import WorkerDetails, JobDetails, User, Categories,RecruitersRequests
from django.db import connection
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
import requests
import json
from django.http import HttpResponse
#from custom_apis.job_views.py import display_job , display_recruiter_job
#from custom_apis.jobviews.py import display_job , display_recruter_job , display_to_recruter , disp_workertorecruiter
# Create your views her

from requests.auth import HTTPBasicAuth
import requests
import json
# Create your views her
AUTH_TOKEN = None

def getin( request):
    return render( request , 'Sign/res.html')


def sign_in(request):
    if request.method == 'POST':

        #Retriving username & password form login form template
        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            'email': username,
            'password':  password,
        }
        # post login details to this api
        url = 'http://127.0.0.1:7000/authapp/token/login/'

        #Store http response which is Authentication token  in result
        result = requests.post(url, json=data)

        #loading Response in json format and storing in auth_info
        auth_info = json.loads(result.content)

        #accessing token and putting it into djoser Authorization format
        AUTH_TOKEN = 'Token {}'.format(auth_info['auth_token'])

        #This Api provides User Information name , is_admin, is_superuser, email, phone etc
        user_info_api = 'http://127.0.0.1:7000/authapp/users/me/'

        #requsting user info form api
        user_info = requests.get(user_info_api, headers={'Authorization': AUTH_TOKEN})

        #storing userinfo response in access in json format
        access = user_info.json()

        #condition so that only admin and superuser can login
        if access['is_admin'] == True or access['is_superuser']==True:
            return redirect('Home')
        else:
            message="You Don’t Have Permission To Access on this Server"
            return HttpResponse(message)
    return render(request , 'Sign/sign_in.html')



def sign_up(request):
    return render(request , 'Sign/sign_up.html')


def forget_pass(request):
    return render( request , 'Sign/forget_pass.html')

def home(request):

        dt=datetime.datetime.now();
        t = datetime.datetime.now().time();
        d={
           'dates':dt,
           'time' : t ,

        }
        return render(request, 'Sign/home.html',context=d)

def register(request):
    return render(request, 'Sign/register.html')

def create(request):
    return render( request , 'Sign/create.html')


def phone_disp(request):
    return render( request , 'Sign/phone_disp.html')



#Display all the workers regradles of there category

def recruiters(request):
    return render(request , 'Sign/recruiters.html')

def workers(request):
    return render(request , 'Sign/workers.html')
