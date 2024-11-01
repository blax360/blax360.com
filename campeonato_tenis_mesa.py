import csv
import random
from typing import List, Dict

class Jugador:
    def __init__(self, nombre: str, club: str, ranking: int):
        self.nombre = nombre
        self.club = club
        self.ranking = ranking
        self.puntos = 0
        self.partidos_ganados = 0
        self.sets_ganados = 0

class Campeonato:
    def __init__(self):
        self.jugadores: List[Jugador] = []
        self.grupos: List[List[Jugador]] = []
        self.mejor_de = 3  # Por defecto, mejor de 3 sets

    def inscribir_jugador(self, nombre: str, club: str, ranking: int):
        self.jugadores.append(Jugador(nombre, club, ranking))

    def importar_jugadores_csv(self, archivo: str):
        with open(archivo, 'r') as f:
            lector = csv.reader(f)
            next(lector)  # Saltar la cabecera
            for fila in lector:
                self.inscribir_jugador(fila[0], fila[1], int(fila[2]))

    def crear_grupos(self, tamaño_grupo: int):
        jugadores_ordenados = sorted(self.jugadores, key=lambda x: x.ranking, reverse=True)
        self.grupos = [jugadores_ordenados[i:i+tamaño_grupo] for i in range(0, len(jugadores_ordenados), tamaño_grupo)]

    def jugar_round_robin(self):
        for grupo in self.grupos:
            for i in range(len(grupo)):
                for j in range(i+1, len(grupo)):
                    self.jugar_partido(grupo[i], grupo[j])

    def jugar_partido(self, jugador1: Jugador, jugador2: Jugador):
        sets_jugador1 = 0
        sets_jugador2 = 0
        for _ in range(self.mejor_de):
            if random.choice([True, False]):
                sets_jugador1 += 1
            else:
                sets_jugador2 += 1
            if sets_jugador1 > self.mejor_de // 2 or sets_jugador2 > self.mejor_de // 2:
                break
        
        if sets_jugador1 > sets_jugador2:
            jugador1.partidos_ganados += 1
            jugador1.puntos += 2
            jugador1.sets_ganados += sets_jugador1
        else:
            jugador2.partidos_ganados += 1
            jugador2.puntos += 2
            jugador2.sets_ganados += sets_jugador2

    def fase_eliminacion(self):
        # Implementar la fase de eliminación simple
        pass

    def mostrar_resultados(self):
        # Implementar la visualización de resultados
        pass

# Ejemplo de uso
if __name__ == "__main__":
    campeonato = Campeonato()
    campeonato.mejor_de = 5  # Cambiar a mejor de 5 sets

    # Inscribir jugadores manualmente
    campeonato.inscribir_jugador("Juan Pérez", "Club A", 1500)
    campeonato.inscribir_jugador("María García", "Club B", 1450)

    # Importar jugadores desde CSV
    campeonato.importar_jugadores_csv("jugadores.csv")

    # Crear grupos
    campeonato.crear_grupos(4)

    # Jugar round robin
    campeonato.jugar_round_robin()

    # Fase de eliminación
    campeonato.fase_eliminacion()

    # Mostrar resultados
    campeonato.mostrar_resultados()
