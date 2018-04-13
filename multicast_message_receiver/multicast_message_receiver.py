#!/usr/bin/env python3
import socket
import binascii
import daiquiri


class multicast_message_receiver(object):

    def __init__(self, group='224.1.1.1', port=5007):
        self.MCAST_GRP = group
        self.MCAST_PORT = port
        self.logger = daiquiri.getLogger()
        self.logger.info("{} init".format(__name__))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except AttributeError as err:
            self.logger.error("Error in Setting up {}".format(str(err)))
            pass

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

        sock.bind((self.MCAST_GRP, self.MCAST_PORT))
        host = socket.gethostbyname(socket.gethostname())

        sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
        sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
                        socket.inet_aton(self.MCAST_GRP) +
                        socket.inet_aton(host))

    def read(self):
        while 1:
            try:
                data=""
                addr = ""
                data, addr = self.sock.recvfrom(1024)
                return True
            except Exception as err:
                self.logger.info("Error Receiving a Message")
                #hexdata = binascii.hexlify(data)
                # print 'Data = %s' % hexdata
                return False
