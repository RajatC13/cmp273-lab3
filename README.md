# cmp273-lab3

Implimentation of UDP using Python's [Twisted Library](https://twistedmatrix.com/documents/15.1.0/core/howto/udp.html)

Q."What happened when you send message from client in Multicast UDP when server is not available?"
A.When you send a message from multicast-client when server is not connected, the client receives the same message that it sends out:
Datagram b'Client: Ping' received from ('192.168.20.16', 8005)
