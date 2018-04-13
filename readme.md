#Multi Cast Classes

I want to play with another product (Apache Nifi) to look at some multi-cast packet intereption. So first I needed a Server and a client.


I do not think there is much too special with this setup, the server is especially easy. The receiver is a little more complex.


## Jenkins

As I continue to explore Jenkins, I did make ine of the tests more complex than normal.

We need to use a Sender and receiver at the same time. So I used the multiprocessing module - with a custom internal method.


```python 


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


```


