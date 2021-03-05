import pygame as pg
import sys

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 30)


def end_game(screen):

    screen.fill((0, 0, 0))
    text = myfont.render(
        "YOU WIN. PRESS ENTER TO EXIT", True, (255, 255, 255))
    screen.blit(text, (220, 280))
    pg.display.update()
    while(1):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()
