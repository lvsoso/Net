#！/usr/bin/env/python3
#coding=utf-8

"""
使用第三方包requests进行地理编码解析
"""

import requests

def geocoder(address):
    """ 使用谷歌api将地址转经纬度
    """
    parameters = {'address':address, 'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocoder('207 N. Defiance St, Archbold, OH')
