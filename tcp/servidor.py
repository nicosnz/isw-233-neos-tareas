import socket

class Servidor:
    def __init__(self):
        self.puerto = 9000
        self.socket_server = None
    def crearConexion(self):
        self.socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_server.bind(("",self.puerto))
        self.socket_server.listen(1)
    def aceptar_conexion(self):
        cliente_socket, direccion = self.socket_server.accept()
        print(f"Cliente conectado desde {direccion}")
        return cliente_socket        
    def cerrarConexion(self):
        self.socket_server.close()