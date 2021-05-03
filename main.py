import requests
from functions import get_district
from datetime import date, datetime
import json
import time

district_code = get_district()

date = date.today()
date = str(date.strftime("%d/%m/%Y"))

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'


def ping_setu(url, district_id, date):
    payload = {'district_id': district_id, 'date': date}
    res = requests.get(url, params=payload)
    data = json.loads(res.text)
    return(data)


def check_slots(data):
    sessions = []
    for center in data['centers']:
        for session in center['sessions']:
            if session['available_capacity'] > 0:
                sessions.append(' {}({}) on {} Capacity {}'.format(
                    center['name'], center['pincode'], session['date'], session['available_capacity']))
    return sessions


def notify(sessions, notified):
    for i in sessions:
        if i not in notified:
            print(i)
            notified.append(i)


def clear_noti(notified):
    notified = []
    last_cleared = datetime.now()
    return notified, last_cleared


last_cleared = datetime.now()
notified = []

while True:
    data = ping_setu(url, district_code, date)
    sessions = check_slots(data)
    notify(sessions, notified)
    time_dif = (datetime.now()-last_cleared)
    if time_dif.total_seconds() > 3600:
        notified, last_cleared = clear_noti(notified)
    time.sleep(10)
