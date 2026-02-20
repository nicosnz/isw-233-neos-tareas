import sys
from servidor import Servidor
from cliente import Cliente
from seaBattleField import SeaBattleField
def StartServer():
    servidor = Servidor()
    servidor.crearConexion()
    socket_cliente = servidor.aceptar_conexion()
    tablero = SeaBattleField()
    tablero.mostrar_tablero()
    
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
    tablero = SeaBattleField()
    tablero.mostrar_tablero()
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
