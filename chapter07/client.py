#coding=utf-8

import argparse
import random
import socket
import zen_utils

import threading

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return 
    for aphorism in random.sample(aphorisms, 3):
        sock.sendall(aphorism)
        print(aphorism, zen_utils.recv_until(sock, b'.'))
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                help='TCP port (default 1060)')
    parser.add_argument('-t', metavar='thread', type=int, default=1, help='create t threads(default=1)')
    args = parser.parse_args()
    address = (args.host, args.p)

    ths = []
    for i in range(args.t):
        ths.append(threading.Thread(target=client, args=(address, args.e)))

    for i in ths:
        i.start()

    for i in ths:
        i.join()

