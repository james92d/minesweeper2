from cfg import *

def clearEmpty():
    if full_grid[2] == '0' and not pygame.sprite.groupcollide(cover_tiles_group, mouse_group, False, False):
        p

    if pygame.sprite.groupcollide(bottom_square_group, mouse_group, False, False) and full_grid[2] == '0':
