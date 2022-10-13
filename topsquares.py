from cfg import *
import events

from funcs import deleteFromTopGrid
from funcs import convertPixelsToRowCols
from funcs import ClearSurroundingEmptyTiles
from funcs import ClearNumberedTiles


class TopSquares(pygame.sprite.Sprite):

    def __init__(self, x, y, item):
        pygame.sprite.Sprite.__init__(self)

        if item == 'mine':
            self.image = pygame.image.load("assets/mine.png")
        if item == '0':
            self.image = pygame.image.load("assets/0.png")
        if item == '1':
            self.image = pygame.image.load("assets/1.png")
        if item == '2':
            self.image = pygame.image.load("assets/2.png")
        if item == '3':
            self.image = pygame.image.load("assets/3.png")
        if item == '4':
            self.image = pygame.image.load("assets/4.png")
        if item == '5':
            self.image = pygame.image.load("assets/5.png")
        if item == '6':
            self.image = pygame.image.load("assets/6.png")
        if item == '7':
            self.image = pygame.image.load("assets/7.png")
        if item == '8':
            self.image = pygame.image.load("assets/8.png")
        if item == 'top':
            self.image = pygame.image.load("assets/top.png")
        if item == 'flag':
            self.image = pygame.image.load("assets/flag.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item = item

    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        for event in events.event_list:  # kills cover tile upon release mouse
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if abs(self.rect.x + 15 - x_pos) <= 15 and abs(self.rect.y + 15 - y_pos) <= 15:

                    if self.item == 'flag':
                        continue

                    else:
                        x, y = convertPixelsToRowCols(self.rect.x, self.rect.y)
                        deleteFromTopGrid(x, y)

                        tile = [x, y, '0']

                        if tile in full_grid:
                            ClearSurroundingEmptyTiles(x, y)
                            ClearNumberedTiles()

            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                if abs(self.rect.x + 15 - x_pos) <= 15 and abs(self.rect.y + 15 - y_pos) <= 15:
                    x, y = convertPixelsToRowCols(self.rect.x, self.rect.y)
                    z = self.item
                    deleteFromTopGrid(x, y)

                    if z == 'top':
                        tile = [x, y, 'flag']
                        top_grid.append(tile)

                    if z == 'flag':
                        tile = [x, y, 'top']
                        top_grid.append(tile)





