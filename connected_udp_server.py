from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        self.host = "192.168.1.1"
        self.port = 1234

        self.transport.connect(self.host, self.port)
        print(f'now we can only send to host {self.host} port {self.port}')
        self.transport.write(bytes('hello from server','utf-8')) # no need for address

    def datagramReceived(self, data, host, port):
        print(f'received {data} from {host}:{port}')

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print('No one listening')

# 0 means any port, we don't care in this case
reactor.listenUDP(0, Helloer())
reactor.run()
