#!/usr/bin/env python3

import requests
import datetime
    
URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp= requests.get(URL).json()
    print(f"CURRENT LOCATION OF THE ISS:\n Lon: {resp['iss_position']['longitude']}\n Lat: + {resp['iss_position']['latitude']}")
    date_time = datetime.datetime.fromtimestamp(resp['timestamp'])
    print(date_time)
main()
