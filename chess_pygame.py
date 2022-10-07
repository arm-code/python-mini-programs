"""
IMPLEMENTING A CHESS BOARD USING PYGAME.
"""
import pygame
import sys
import numpy as np

BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE_BOARD = 8

pygame.init()
sizeScreen = [400,400]
displayTable = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption("Chess Board")
game_state =  np.zeros((SIZE_BOARD,SIZE_BOARD))
print(game_state)
endgame = False

clock = pygame.time.Clock()
widthTable = int(sizeScreen[0] / SIZE_BOARD)
heightTable = int(sizeScreen[1] / SIZE_BOARD)

while endgame is False:

    for eventGame in pygame.event.get():
        if eventGame.type  == pygame.QUIT:
            endgame = True
            sys.exit()

    displayTable.fill(WHITE)

    # RELLENA LA PANTALLA CON CUADROS BLANCOS Y NEGROS
    color = 0
    for i in range (0, sizeScreen[0], widthTable):
        for j in range(0, sizeScreen[1], heightTable):
            if color % 2  == 0:
                pygame.draw.rect(displayTable, BLACK, [i, j, widthTable, heightTable], 0)
            else:
                pygame.draw.rect(displayTable, WHITE, [i, j, widthTable, heightTable], 0)
            color += 1
        color += 1
    
    # DIBUJA UN CIRCULO ROJO EN MEDIO DE UN CUADRADO
    # circle(surface, color, center, radius)
    pygame.draw.circle(displayTable,(255,0,0),(25,25), 10)
    pygame.draw.circle(displayTable,(255,0,0),(75,75), 10)
    pygame.draw.circle(displayTable,(255,0,0),(125,125), 10)
    pygame.draw.circle(displayTable,(255,0,0),(25,75), 10)
    pygame.draw.circle(displayTable,(255,0,0),(75,25), 10)
    

    # ACTUALIZA LA PANTALLA 
    pygame.display.flip()

    clock.tick(5)
pygame.quit()



