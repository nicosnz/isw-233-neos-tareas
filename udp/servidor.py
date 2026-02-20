import socket
class Servidor:
    def __init__(self,puerto):
        self.ip = "192.168.0.132"
        self.puerto = puerto
    def crearSocket(self):
        server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        server_sock.bind((self.ip,self.puerto))
        return server_sock