import requests
import json
import os
import pwd
from .jobviews import disp_id

json_data = {}

URL = ""
 def send_id(namw):
     data = {}
     # getting workers id by using current loggged user
         d = pwd.getpwuid( os.getuid() )[ 0 ]

      id = {

              'worker_id' : d,
              'recruiter_name' : username
      }

      #Converting Both id in json format..
      json_data = json.dumps(id)

      #sending a get request to url and storing responsse in r
      r = requests.get( url = URL , data = json_data)

     # converting json data into python dictionary
      data =  r.json()
      print(data)


send_id('aadesh')
