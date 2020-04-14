
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import json


# In[ ]:


import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/'

params = {
    'address': '36 College Ave, Somerville, MA',
    'sensor': 'false',
    'region': 'US',
    'key': 'AIzaSyAS2ya8Mmxm5nnLMqO3xd8RSarL6S3-oVU'
}

# Do the request and get the response data
req = requests.get(GOOGLE_MAPS_API_URL, params=params)
print(req)
#res = req.json()

# Use the first result
#result = req['results'][0]

#geodata = dict()
#geodata['lat'] = res['geometry']['location']['lat']
#geodata['lng'] = res['geometry']['location']['lng']#3geodata['address'] = res['formatted_address']

#print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
# 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)


# In[ ]:



    
#Request
url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCU6DSIZ8LxSL8BqeHDA-Vgbm2aVvZjgnY'
    
params = {
    'address': '36 College Ave, Somerville, MA',
    'sensor': 'false',
    'region': 'US',
    'key': 'AIzaSyCU6DSIZ8LxSL8BqeHDA-Vgbm2aVvZjgnY'
}

req = requests.get(url, params = params)
# print(req.json())
json = req.json()


# In[ ]:


l = [{'a': 4}, {'b': 4}]
for p in l:
    if 'b' in p:
        print(p)
    else:
        continue
        


# In[6]:


dic = {'c': 3}
dic['c']


# In[7]:


def json_to_name(json):
    json['results']
    #
    result = json['results']
    #
    for add in result:
        if 'address_components' in add:
            elements = add
        else:
            continue
    address_components = elements['address_components']
    #
    target = ""
    for temlist in address_components:
    #     if 'types' in temlist:
        types = temlist['types']
        if types == ['neighborhood', 'political']:
            target = temlist
        else:
            continue
    name = target['long_name']
    return name


# In[8]:


def address_to_name(somerville_address):
    address = somerville_address + ', Somerville, MA'
    params = {
        'address': address,
        'sensor': 'false',
        'region': 'US',
        'key': 'AIzaSyCU6DSIZ8LxSL8BqeHDA-Vgbm2aVvZjgnY'
    }

    req = requests.get(url, params = params)
    json = req.json()
    name = json_to_name(json)
    return name


# In[ ]:


address_to_name('Elm St')


# In[ ]:


addresses = ['81 Newburry St', '123 Elm St']
neighborhoods = []
for a in addresses:
    neighborhood = address_to_name(a)
    neighborhoods.append(neighborhood)
neighborhoods

