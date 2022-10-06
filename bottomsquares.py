from cfg import *
import events

from clearempty import ClearEmpty


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

        left = (True, False, False)
        right = (False, False, True)
        both = (True, False, True)
        none = (False, False, False)

        mouse_pos = pygame.mouse.get_pos()
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]

        buttons = pygame.mouse.get_pressed()

        if pygame.sprite.spritecollide(self, mouse_group, False):  # mouse colliding with any bottom square
            if not events.collide_mouse_cover:  # mouse not colliding with any top squares
                if self.item == '0':
                    #  kill all surrounding cover tiles
                    x = self.rect.x
                    y = self.rect.y
                    # ClearEmpty(x, y)

                    # kill cover tile (x, y)
                    for i in top_grid:
                        x = i[0]
                        y = i[1]
                        print(x, y)

                        if [x - 1, y - 1, 'top'] in top_grid:
                            print('test')
                            # # i.kill()
                            ClearEmpty(x - 1, y - 1)
                        if [x - 1, y, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x - 1, y)
                        if [x - 1, y + 1, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x - 1, y + 1)
                        if [x, y - 1, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x, y - 1)
                        if [x, y + 1, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x, y + 1)
                        if [x + 1, y - 1, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x + 1, y - 1)
                        if [x + 1, y, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x + 1, y)
                        if [x + 1, y + 1, 'top'] in top_grid:
                            print('test')
                            # i.kill()
                            ClearEmpty(x + 1, y + 1)

