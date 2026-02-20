import socket
import numpy as np
class Cliente:
    def __init__(self,puerto):
        self.puerto = puerto
    def enviarAudio(self,stream,max_frames):
        ip = input("Ingresa IP del servidor: ")
        cliente_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        
        print("Grabando Audio...")

        while True:
            # data = stream.read(max_frames)
            # cliente_sock.sendto(data,(ip,self.puerto))
            noise = np.random.randint(-128, 127, max_frames, dtype=np.int8)
            cliente_sock.sendto(noise.tobytes(), (ip,self.puerto))
            # print("Bytes enviados: ",len(data))
        