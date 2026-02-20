import socket

class Servidor:
    def __init__(self):
        self.puerto = 8000
        self.socket_server = None
        self.cliente_socket = None
    
    def crearConexion(self):
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_server.bind(("",self.puerto))
        self.socket_server.listen(1)
        
    
    def aceptarConexion(self):
        cliente_socket, direccion = self.socket_server.accept()
        self.cliente_socket = cliente_socket
    def recibirMensaje(self):
        if not self.cliente_socket:
            raise OSError("No hay cliente conectado para recibir mensaje")
        recibido = self.cliente_socket.recv(1024)
        return recibido.decode()
    
    def enviarMovimiento(self):
        movimiento = input("Tu turno. Introduce tu movimiento ")
        self.cliente_socket.send(movimiento.encode("utf-8"))
        return movimiento
        
    def enviarRespuestaAtaque(self, isShoot):
        respuesta = "True" if isShoot else "False"
        self.cliente_socket.send(respuesta.encode('utf-8'))
    def recibirRespuestaAtaque(self):
        if not self.cliente_socket:
            raise OSError("No hay cliente conectado para recibir respuesta")
        recibido = self.cliente_socket.recv(1024)
        respuesta = recibido.decode()
        return respuesta == "True"
            
           
    def cerrarConexion(self):
        self.socket_server.close()
        self.cliente_socket.close()