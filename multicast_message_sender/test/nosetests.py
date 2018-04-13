from multicast_message_sender import multicast_message_sender
mcast_obj=None


def test_000_init_good():
    global mcast_obj
    mcast_obj = multicast_message_sender()
    assert mcast_obj

def test_010_send_good():
    global mcast_obj
    assert mcast_obj.send_msg("tim was here")


def test_010_send_10_good():
    global mcast_obj
    for n in range(10):
        assert mcast_obj.send_msg("tim{} was here".format(n))


