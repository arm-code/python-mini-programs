
"""
IMPLEMENTING A CHESS BOARD USING PYGAME. 
THIS VERSION WAS DOWNLOADED FROM INTERNET.
"""
import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
sizeScreen = [200,200]
displayTable = pygame.display.set_mode(sizeScreen)
pygame.display.set_caption("Table")

endgame = False

clock = pygame.time.Clock()
widthTable = int(sizeScreen[0] / 8)
heightTable = int(sizeScreen[1] / 8)
while endgame is False:
    for eventGame in pygame.event.get():
        if eventGame  == pygame.QUIT:
            endgame = True
    displayTable.fill(WHITE)
    color = 0
    for i in range (0, sizeScreen[0], widthTable):
        for j in range(0, sizeScreen[1], heightTable):
            if color % 2  == 0:
                pygame.draw.rect(displayTable, BLACK, [i, j, widthTable, heightTable], 0)
            else:
                pygame.draw.rect(displayTable, WHITE, [i, j, widthTable, heightTable], 0)
            color += 1
        color += 1
    pygame.display.flip()
    clock.tick(5)
pygame.quit()



