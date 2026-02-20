import sys
from servidor import Servidor
from audio import Audio
from cliente import Cliente
def StartServer(puerto):
    servidor = Servidor(puerto)
    sock_Server = servidor.crearSocket()
    audio = Audio()
    stream = audio.salidaAudio()
    print("Servidor Escuchando...")
    while True:
        data,direccion = sock_Server.recvfrom(65507)
        
        frames = len(data) // audio.frames
        print("Frames recibidos: ",frames)
        stream.write(data)
        
def StartClient(puerto):
    cliente = Cliente(puerto)
    audio = Audio()
    stream = audio.crearAudio()
    cliente.enviarAudio(stream,audio.max_frames)


def main():
    
    if len(sys.argv) != 3:
        print("Uso: python main.py [client|server] <port>")
        sys.exit(1)

    modo= sys.argv[1]
    puerto = int(sys.argv[2])

    if modo== "server":
        StartServer(puerto)
    elif modo== "client":
        StartClient(puerto)
    else:
        print("Modo inválido. Usa 'client' o 'server'.")
    
if __name__ == "__main__":
    main()