import pygame

name = "Minesweeper"
fps = 120
columns = 30
rows = 24
num_of_mines = 99
square_size = 30
square_plus2 = square_size + 2

window_height = (2 + rows) * square_plus2
window_width = (2 + columns) * square_plus2

grey_1 = (150, 150, 150)
grey_2 = (100, 100, 100)
grey_3 = (50, 50, 50)
white = (255, 255, 255)
black = (0, 0, 0)

top_grid = []
full_grid = []
counter = 0

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(name)

bottom_square_group = pygame.sprite.Group()
cover_tiles_group = pygame.sprite.Group()
clicking_square_group = pygame.sprite.Group()
mouse_group = pygame.sprite.Group()
