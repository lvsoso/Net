#coding=utf-8

import select
import zen_utils

def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event

def server(listener):
    sockets = {listener.fileno():listener}
    address = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    # Socket closed: remove it from our data structures.
    for fd, event in all_events_forever(pool_object):
        sock = sockets[fd]

        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print('Client {} sent {} but then closed'.format(address, rb))
            elif sb:
                print('Client {} closed before we sent {}'.format(address, sb))
            else:
                print('Client {} closed socket normally'.format(address))
            poll_object.unregister(fd)
            del sockets[fd]
    # New socket: add it to our data structures.

    elif sock is listener:
        sock, address = sock.accept()
        print('Accepted connection from {}'.format(address))
        sock.setblocking(False)     # force socket.timeout if we blunder
        sockets[sock.fileno()] = sock
        addresses[sock] = address
        poll_object.register(sock, select.POLLIN)