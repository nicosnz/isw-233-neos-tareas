import sys
from servidor import Servidor
from cliente import Cliente
def StartServer():
    servidor = Servidor()
    servidor.crearConexion()
    socket_cliente = servidor.aceptar_conexion()
    while True:
        recibido = socket_cliente.recv(1024)
        if recibido.decode() == "close":
            break
        print(recibido.decode())
        socket_cliente.send(recibido)
    socket_cliente.close()
    servidor.cerrarConexion()
def StartClient():
    cliente = Cliente()
    cliente.crearConexion()
    while True:
        mensaje = cliente.enviarMensaje()
        if mensaje == "close":
            break
    cliente.cerrarConexion()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        modo = sys.argv[1]
        if modo == "cliente":
            StartClient()
        elif modo == "servidor":
            StartServer()
