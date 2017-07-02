#！/usr/bin/env/python3
#coding=utf-8

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocoder/json'

def geocoder(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocoder('207 N. Defiance St, Archbold, OH')