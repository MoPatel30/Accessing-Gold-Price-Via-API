import sys
import urllib.request
import requests

import ssl
import json
import time
import math


ssl._create_default_https_context = ssl._create_unverified_context


try:
  from urllib3 import PoolManager
  from json import loads as json
  from time import time

except:
  print("unable to import default modules")
  exit()

#Set constants
http = PoolManager()
URL = "https://metals-api.com/api/latest?access_key=(access key removed)"

API_KEY = "Enter Access Key Here"


class getgold_price(object):

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        if not self.API_KEY:
            print("No API key given. Register at metals-api.com")
            return
    

        self.api_data = self.grab(API_KEY)
        self.json = json(self.api_data)
        self.price = self.json['rates']['XAU']
       


    def grab(self, API_KEY):
        self.r = http.request("GET", URL, headers={
        'Accepts': 'application/json',
        'Metals_API_API_KEY': API_KEY}
        )
        return self.r.data.decode()
    

temp = getgold_price(API_KEY).price
temp2 = round((1.0 / temp), 2)
print("Current price of one ounce of Gold (XAU) in USD is: " + str(temp2) + " USD")



