from cfg import *
import events

from funcs import deleteFromTopGrid
from funcs import convertPixelsToRowCols
from funcs import ClearSurroundingEmptyTiles
from funcs import ClearNumberedTiles


class BottomSquares(pygame.sprite.Sprite):

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

        x = self.rect.x
        y = self.rect.y
        z = self.item

        surrounding_tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        surrounding_tiles[1] = [x - 1, y - 1, 'flag']
        surrounding_tiles[2] = [x - 1, y, 'flag']
        surrounding_tiles[3] = [x - 1, y + 1, 'flag']
        surrounding_tiles[4] = [x, y - 1, 'flag']
        surrounding_tiles[5] = [x, y + 1, 'flag']
        surrounding_tiles[6] = [x + 1, y - 1, 'flag']
        surrounding_tiles[7] = [x + 1, y, 'flag']
        surrounding_tiles[8] = [x + 1, y + 1, 'flag']

        counter1 = 0

        for i in range(1, 9):
            if surrounding_tiles[i] in top_grid:
                counter1 += 1

        j = [x, y, z]

        mouse_pos = pygame.mouse.get_pos()
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        for event in events.event_list:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if abs(self.rect.x + 15 - x_pos) <= 15 and abs(self.rect.y + 15 - y_pos) <= 15:
                    print('test')
                    # if counter == str(self.item):
                        # Kill surrounding tiles
                        # print('test')



