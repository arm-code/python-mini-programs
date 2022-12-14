#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/07/14/tutorial-pygame-4-figuras-y-texto

# ---------------------------
# Importación de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

WIDTH = 640
HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


class Proyectil(pygame.sprite.Sprite):
    "Clase que representa el proyectil lanzado"

    def __init__(self, x, y):
        self.angulo = 45
        self.veloc = 50
        self.tiempo = 0
        self.x = x
        self.y = y
        self.xreal = x
        self.yreal = HEIGHT - self.y


# ------------------------------
# Función principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 4")

    # se define la letra por defecto
    fuente = pygame.font.Font(None, 20)

    # se crea un proyectil a lanzar
    bala = Proyectil(0, HEIGHT)

    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

        text = "Velocidad: %3d (m/s)   Angulo: %d   x=%d m   y=%d m" % (
            bala.veloc, bala.angulo, bala.xreal, bala.yreal)
        mensaje = fuente.render(text, 1, (255, 255, 255))

        # Re dibujar los elementos en pantalla
        screen.fill((30, 145, 255))
        screen.blit(mensaje, (15, 5))
        pygame.draw.line(screen, (255, 255, 255), (0, 25), (640, 25), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(bala.x), int(bala.y)), 10)
        # actualizamos la pantalla
        pygame.display.flip()


if __name__ == "__main__":
    main()