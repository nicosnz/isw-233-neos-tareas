import sys
from servidor import Servidor
from cliente import Cliente
from seaBattleAgent import SeaBattleAgent
def StartServer():
    seaBattleAgent = SeaBattleAgent()
    seaBattleAgent.startGame("servidor")
    
def StartClient():
    
    seaBattleAgent = SeaBattleAgent()
    seaBattleAgent.startGame("cliente")    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        modo = sys.argv[1]
        if modo == "cliente":
            StartClient()
        elif modo == "servidor":
            StartServer()
