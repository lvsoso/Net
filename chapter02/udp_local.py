#！/usr/bin/env/python3
#coding=utf-8

import argparse
import socket
from datetime import datetime

import time # for test udp client recv from another server

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        #time.sleep(180)
        #>>> import socket
        #>>> sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #>>> sock.sendto('FAKE'.encode('ascii'), ('127.0.0.1',61638 ))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == '__main__':
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
