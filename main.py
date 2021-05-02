import requests
from functions import get_district
from datetime import date
import json

district_code = get_district()

date = date.today()
date = str(date.strftime("%d/%m/%Y"))

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

def ping_setu(url,district_id,date):
    payload = {'district_id':district_id , 'date':date }
    res = requests.get(url, params=payload)
    data = json.loads(res.text)
    return(data)

data = ping_setu(url,district_code,date)
for center in data['centers']:
    for session in center['sessions']:
        if session['available_capacity']>0:
            print(' {}({}) on {} Capacity {}'.format(center['name'],center['pincode'],session['date'], session['available_capacity']))
