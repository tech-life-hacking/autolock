import socket

class Receiver():
    def __init__(self, address, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((address, port))

    def receive(self):
        msg, addr = self.s.recvfrom(1024)
        return msg.decode("utf-8")

    def close(self):
        self.s.close()