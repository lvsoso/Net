#！/usr/bin/env/python3
#coding=utf-8

import socket

if __name__ == '__main__':
    host_name = 'maps.google.com'
    addr = socket.gethostbyname(host_name)
    print('The IP address of {} is {}'.format(host_name, addr))