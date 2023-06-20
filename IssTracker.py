#!/usr/bin/env python

import urllib3
import json
from colorama import init, Fore

http = urllib3.PoolManager()

class Tracker:
    global http    

    def __init__(self, sid,):
        self.sid = sid
    
    
    def credit():
        print('''
        {ISS TRACKER V.01}
        {CREATED BY NEOS}
        ''')


    def track_satellite(self,):
        Tracker.credit()
        # INITIATE HTTP 'GET' REQUEST
        resp = http.request('GET', 'https://api.wheretheiss.at/v1/satellites/25544')
        json_data = json.loads(resp.data)
        
        # PRINT DATA
        print('NAME: <%s>' % (json_data['name']))
        print('LATITUDE <%.6f>' % (json_data['latitude']))
        print('LONGITUDE <%.6f>' % (json_data['longitude']))


    def locate_coordinates(self,):
        Tracker.credit()

        # SEND THE GET REQUEST AND RETURN JSON DATA
        resp = http.request('GET', 'https://api.wheretheiss.at/v1/satellites/25544')
        json_data = json.loads(resp.data)
        latitude_coordinates = json_data['latitude']
        longitude_coordinates = json_data['longitude']
        
        # INITIATE HTTP 'GET' REQUEST
        resp = http.request('GET', 'https://api.wheretheiss.at/v1/coordinates/%.6f, %.6f' % (latitude_coordinates, longitude_coordinates))
        json_data = json.loads(resp.data)
        
        # PRINT DATA
        print()
        print('TIMEZONE ID: <%s>' % (json_data['timezone_id']))
        print('COUNTRY CODE: <%s>' % (json_data['country_code']))
        print('MAP URL: <%s>' % (json_data['map_url']))


        
