class SeaBattleField:
    def __init__(self, filas=8, columnas=8):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self.__generar_tablero()
        self.barcos = []  # Lista de barcos colocados
        
        self.estructura_barcos = [
            (4, 1),  # 1 acorazado de 4 casillas
            (3, 2),  # 2 cruceros de 3 casillas
            (2, 3),  # 3 destructores de 2 casillas
            (1, 4)   # 4 submarinos de 1 casilla
        ]
        
        self.__colocar_todos_barcos_automatico()
        # Crear tablero vacío para el oponente UNA VEZ que los barcos propios están colocados
        # así nos aseguramos de que el tablero del oponente no contiene barcos por accidente
        self.oponente_tablero = self.__generar_tablero()
    
    def __generar_tablero(self):
        tablero = [[' ' for _ in range(self.columnas)] for _ in range(self.filas)]
        return tablero
    
    def mostrar_tablero(self):
        # Encabezado con letras para columnas
        letras = [chr(65 + i) for i in range(self.columnas)]  # A, B, C, D...
        print("  " + " ".join(letras))
        
        # Filas con números
        for i, fila in enumerate(self.tablero):
            print(f"{i} " + " ".join(fila))

    def mostrar_tableros_lado_a_lado(self):
        """Muestra el tablero propio y el tablero (vacío) del oponente lado a lado."""
        letras = [chr(65 + i) for i in range(self.columnas)]
        # Cabeceras
        izquierda = "  " + " ".join(letras)
        derecha = "  " + " ".join(letras)
        print(izquierda + ("   ") + derecha)

        # Filas: usar el tablero del oponente almacenado en el atributo
        for i in range(self.filas):
            fila_izq = " ".join(self.tablero[i])
            fila_der = " ".join(self.oponente_tablero[i])
            print(f"{i} {fila_izq}   {i} {fila_der}")
    
    def __obtener_celdas_ocupadas(self, fila, columna, tamaño, horizontal):
        celdas = []
        if horizontal:
            for i in range(tamaño):
                celdas.append((fila, columna + i))
        else:
            for i in range(tamaño):
                celdas.append((fila + i, columna))
        return celdas
    
    def __obtener_zona_proximidad(self, celdas):
        zona = set()
        for fila, columna in celdas:
            for f in range(fila - 1, fila + 2):
                for c in range(columna - 1, columna + 2):
                    if 0 <= f < self.filas and 0 <= c < self.columnas:
                        zona.add((f, c))
        return zona
    
    def __puede_colocar_barco(self, fila, columna, tamaño, horizontal):
        
        # Verificar que no salga del tablero
        if horizontal:
            if columna + tamaño > self.columnas:
                return False
        else:
            if fila + tamaño > self.filas:
                return False
        
        # Obtener celdas que ocuparía el barco
        celdas = self.__obtener_celdas_ocupadas(fila, columna, tamaño, horizontal)
        
        # Obtener zona de proximidad (donde no pueden estar otros barcos)
        zona_proximidad = self.__obtener_zona_proximidad(celdas)
        
        # Verificar que no haya barcos en la zona de proximidad
        for celda_ocupada, _ in self.barcos:
            for f, c in celda_ocupada:
                if (f, c) in zona_proximidad:
                    return False
        
        return True
    
    def __colocar_barco(self, fila, columna, tamaño, horizontal=True):
        """Coloca un barco si es posible. Retorna True si se colocó, False si no"""
        
        if not self.__puede_colocar_barco(fila, columna, tamaño, horizontal):
            return False
        
        # Obtener celdas del barco
        celdas = self.__obtener_celdas_ocupadas(fila, columna, tamaño, horizontal)
        
        # Guardar el barco
        self.barcos.append((celdas, tamaño))
        
        # Marcar en el tablero
        for f, c in celdas:
            self.tablero[f][c] = "B"
        
        return True
    
    def __colocar_todos_barcos_automatico(self):
        """Intenta colocar automáticamente todos los barcos de forma aleatoria"""
        import random
        
        for tamaño, cantidad in self.estructura_barcos:
            colocados = 0
            intentos = 0
            max_intentos = 100
            
            while colocados < cantidad and intentos < max_intentos:
                fila = random.randint(0, self.filas - 1)
                columna = random.randint(0, self.columnas - 1)
                horizontal = random.choice([True, False])
                
                if self.__colocar_barco(fila, columna, tamaño, horizontal):
                    colocados += 1
                
                intentos += 1
            
            if colocados < cantidad:
                print(f"Advertencia: Solo se colocaron {colocados}/{cantidad} barcos de tamaño {tamaño}")
        
        return len(self.barcos) == 10

  
        """Marca un tiro en el tablero del oponente en coordenadas (x, y).

        Convención: x = columna, y = fila (0-based).

        Antes de marcar, verifica que (x,y) esté dentro del tablero, que aún
        no haya sido disparado y que NO esté en la zona de proximidad de ninguno
        de los barcos propios (no debe tocar mis barcos).

        Retorna:
        - True si el tiro fue marcado con éxito en `oponente_tablero` (marca 'O').
        - False si la coordenada es inválida, ya fue disparada o está en zona de proximidad.
        """
        # Validar límites
        if not (0 <= x < self.columnas and 0 <= y < self.filas):
            return False

        # Verificar si ya se disparó ahí
        if self.oponente_tablero[y][x] != ' ':
            return False

        # Construir la zona prohibida (proximidad) de todos los barcos propios
        zona_prohibida = set()
        for celdas, _ in self.barcos:
            zona_prohibida |= self.__obtener_zona_proximidad(celdas)

        # Si la celda está en zona prohibida, no permitir el disparo
        if (y, x) in zona_prohibida:
            return False

        # Marcar el disparo como 'O' (por defecto, sin info del oponente)
        self.oponente_tablero[y][x] = 'O'
        return True