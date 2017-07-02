#！/usr/bin/env/python3
#coding=utf-8

"""
使用第三方包pygeocoder进行地理编码解析
"""

from pygeocoder import Geocoder

if __name__ == "__main__":
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
