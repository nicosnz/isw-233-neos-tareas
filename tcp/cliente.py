import socket

class Cliente:
    def __init__(self):
        self.puerto = 9000
        self.ip = "192.168.0.132"
        self.socket_server = None
    def crearConexion(self):
        self.socket_server = socket.socket()
        self.socket_server.connect((self.ip,self.puerto))
    def enviarMensaje(self):
        mensaje = input("Mensaje a enviar: ")
        self.socket_server.sendall(mensaje.encode('utf-8')) 
        return mensaje      
    def cerrarConexion(self):
        self.socket_server.close()