from multicast_message_receiver import multicast_message_receiver
from multicast_message_sender   import multicast_message_sender
import multiprocessing
import time
import daiquiri

mm_receiver=None
mcs=None
logger=daiquiri.getLogger()

def test_000_init_good():
    global mm_receiver
    mm_receiver = multicast_message_receiver()
    assert mm_receiver


def test_005_init_server():
    global mcs
    mcs = multicast_message_sender()
    assert mcs


def test_010_init_good():
    global mcs, mm_receiver

    def lcl_send():
        global mcs
        for n in range(10):
            mcs.send_msg(msg="Hi {}".format(n))
            time.sleep(0.2)


    Server_Process = multiprocessing.Process(name='server', target=lcl_send)
    Server_Process.daemon = True
    Server_Process.start()


    Client_Process = multiprocessing.Process(name='client', target=mm_receiver.read)
    Client_Process.daemon = False


    Client_Process.start()

    Server_Process.join()
    logger.info("Server Finished")
    Client_Process.terminate()
    logger.info("Client Finished")

    assert True