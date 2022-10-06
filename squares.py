import pygame
from cfg import *


class Squares(pygame.sprite.Sprite):

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

        left = (True, False, False)
        right = (False, False, True)
        both = (True, False, True)

        mouse_pos = pygame.mouse.get_pos()
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        buttons = pygame.mouse.get_pressed()

        # if buttons == left and abs(self.rect.x + 15 - x_pos) < 15 and abs(self.rect.y + 15 - y_pos) < 15:
        #     self.kill()
        #     print('test')
        #     print(len(cover_tiles_group))

        if pygame.sprite.spritecollide(self, mouse_group, False):
            self.kill()
            print('kill')

        # counter = 0
        #
        # if buttons == right:
        #     for obj in cover_tiles_group:
        #         self.kill()
        #         counter += 1
        #         print('counter : ', counter)
