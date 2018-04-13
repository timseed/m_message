import socket
import struct
import daiquiri

class multicast_message_sender(object):

    def __init__(self, group='224.1.1.1', port=5007):
        self.MCAST_GRP = group
        self.MCAST_PORT = port
        self.logger = daiquiri.getLogger()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        self.logger.info("Starting MCast")

    def send_msg(self,msg='blank message'):

        if type(msg) == str:
            self.logger.debug("Converting data to bytes before sending")
            msg = msg.encode('utf-8')

        try:
            self.sock.sendto(msg,(self.MCAST_GRP, self.MCAST_PORT))
            self.logger.info("Multicast send message OK")
        except Exception as err:
            self.logger.error("Error sending a message {}".format(str(err)))
            return False
        return True


