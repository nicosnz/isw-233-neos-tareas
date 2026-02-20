import socket

class Cliente:
    def __init__(self):
        self.puerto = 8000
        self.ip = "localhost"
        self.socket_server = None
    
    def crearConexion(self):
        self.socket_server = socket.socket()
        self.socket_server.connect((self.ip,self.puerto))
    
    def enviarMovimiento(self):
        mensaje = input("Tu turno. Introduce tu movimiento: ")
        self.socket_server.send(mensaje.encode('utf-8'))
        return mensaje
    
    def recibirMovimientoServidor(self):
        recibido = self.socket_server.recv(1024)
        mensaje = recibido.decode()
        return mensaje
    def enviarRespuestaAtaque(self, isShoot):
        respuesta = "True" if isShoot else "False"
        self.socket_server.send(respuesta.encode('utf-8'))
    
    def recibirRespuestaAtaque(self):
        recibido = self.socket_server.recv(1024)
        respuesta = recibido.decode()
        return respuesta == "True"
            
    def cerrarConexion(self):
        self.socket_server.close()