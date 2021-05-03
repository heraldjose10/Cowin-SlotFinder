import requests
import json

def get_req(url,params = None):
    if params:
        res = requests.get(url,params=params)
    else:
        res = requests.get(url)
    res = json.loads(res.text)
    return(res)

def get_district():
    district = input('District code : ')
    return district

def get_phone():
    phone = input('Your phone num : ')
    phone = '+91{}'.format(phone)
    return phone

