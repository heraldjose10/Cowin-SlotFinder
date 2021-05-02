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

def find_district():

    url = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
    states = get_req(url)
    for i in states['states']:
        state_id = i['state_id']
        state_name = i['state_name']
        print('{state: <22} : {n: <2}'.format(state = state_name,n = state_id))
    
    state_id = input('Input your States ID : ')
    url = 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}'.format(state_id)
    districts = get_req(url)
    for i in districts['districts']:
        district_id = i['district_id']
        district_name = i['district_name']
        print('{} : {}'.format(district_name,district_id))
