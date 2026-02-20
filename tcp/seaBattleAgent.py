from seaBattleField import SeaBattleField
from servidor import Servidor
from cliente import Cliente

class SeaBattleAgent:
    servidor:Servidor
    cliente:Cliente
    tablero:SeaBattleField
    isGameEnded:bool
    def __init__(self,servidor:Servidor = Servidor(),cliente:Cliente = Cliente()):
        self.tablero = SeaBattleField()
        self.isGameEnded = False
        self.servidor = servidor
        self.cliente = cliente
       
    def startGame(self,instancia):
        self.tablero.mostrar_tableros_lado_a_lado()
        if instancia == "servidor":
            
            self.servidor.crearConexion()
            self.servidor.aceptarConexion()
        elif instancia == "cliente":
            self.cliente.crearConexion()
        turno = "cliente"
        while not self.isGameEnded:
            
            if turno == "servidor" and instancia == "servidor":
                movimiento = self.servidor.enviarMovimiento()
                columna,fila = self.parse_move(movimiento)
                isShoot = self.cliente.recibirRespuestaAtaque()
                if isShoot:
                    self.tablero.oponente_tablero[fila][columna] = 'X'
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "servidor"
                else:
                    self.tablero.oponente_tablero[fila][columna] = 'O'
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "cliente"

                turno = "cliente"
            elif turno == "servidor" and instancia == "cliente":
                movimientoServidor = self.cliente.recibirMovimientoServidor()
                columna,fila = self.parse_move(movimientoServidor)
                isShoot = self.shoot(columna,fila)
                if isShoot :
                    self.tablero[fila][columna] = "X"
                    self.servidor.enviarRespuestaAtaque(isShoot)
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "servidor"
                else:
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "cliente"
            elif turno == "cliente" and instancia == "servidor":
                movimientoCliente = self.servidor.recibirMensaje()
                columna,fila = self.parse_move(movimientoCliente)
                isShoot = self.shoot(columna,fila)
                if isShoot :
                    self.tablero[fila][columna] = "X"
                    self.servidor.enviarRespuestaAtaque(isShoot)
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "cliente"
                else:
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "servidor"
            elif turno == "cliente" and instancia == "cliente":
                movimiento = self.cliente.enviarMovimiento()
                columna,fila = self.parse_move(movimiento)
                isShoot = self.cliente.recibirRespuestaAtaque()
                if isShoot:
                    self.tablero.oponente_tablero[fila][columna] = 'X'
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "cliente"
                else:
                    self.tablero.oponente_tablero[fila][columna] = 'O'
                    self.tablero.mostrar_tableros_lado_a_lado()
                    turno = "servidor"
    
    def shoot(self, columna, fila):
        
        if columna < 0 or columna > 7 or fila < 0 or fila > 7:
            print("Coordenadas fuera de rango")
            return False
        
        for celdas, tamaño in self.tablero.barcos:
            if (fila, columna) in celdas:
                return True
        
        
        return False
        
    
    def parse_move(self, coordenadas):
        
        try:
            if len(coordenadas) != 2:
                print(f"Formato inválido: '{coordenadas}'. Use formato como 'B8'")
                return None
            
            letra, numero = coordenadas[0].upper(), coordenadas[1]
            
            columna = ord(letra) - ord('A')
            
            fila = int(numero)
            
            if columna < 0 or columna > 7 or fila < 0 or fila > 7:
                print(f"Coordenadas fuera de rango: '{coordenadas}'. Rango válido: A1-H8")
                return None
            
            return (columna, fila)
        
        except (ValueError, IndexError):
            print(f"Error al parsear coordenadas: '{coordenadas}'")
            return None