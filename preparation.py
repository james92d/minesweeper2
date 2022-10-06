from cfg import *
import random

from mouse import Mouse
from squares import Squares


def drawBackground():
    window.fill(grey_3)


def createGrid():  # Create the full background grid of the game
    mine_tiles = []  # tiles with mines in them
    wall_tiles = []  # boundary outside full grid
    play_grid = []  # full_grid minus wall tiles
    mine_counter = 0

    for i in range(0, columns + 2):  # generating the 4 grids declared above
        for j in range(0, rows + 2):
            wall_tiles.append([i, j, 'wall'])
            full_grid.append([i, j, 'null'])

    for i in range(1, columns + 1):  # generating the 4 grids declared above
        for j in range(1, rows + 1):
            wall_tiles.remove([i, j, 'wall'])
            play_grid.append([i, j, 'null'])

    while mine_counter < num_of_mines:  # generating the desired number of mines
        x = random.randint(0, len(play_grid) - 1)
        if play_grid[x][2] != 'mine':
            play_grid[x][2] = 'mine'
            mine_counter += 1

    for i in range(0, len(full_grid)):  # add mines from play_grid to full_grid

        if [full_grid[i][0], full_grid[i][1], 'mine'] in play_grid:
            full_grid[i][2] = 'mine'
            mine_tiles = mine_tiles + [full_grid[i][0], full_grid[i][1], 'mine']

    for i in range(0, len(full_grid)):  # add walls from wall_tiles to full_grid

        if [full_grid[i][0], full_grid[i][1], 'wall'] in wall_tiles:
            full_grid[i][2] = 'wall'

    for i in range(0, len(full_grid)):  # check for surrounding mines

        if full_grid[i][2] != 'mine' and full_grid[i][2] != 'wall':

            x = full_grid[i][0]
            y = full_grid[i][1]
            adjacent_mines = 0

            if [x - 1, y - 1, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x - 1, y, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x - 1, y + 1, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x, y - 1, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x, y + 1, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x + 1, y - 1, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x + 1, y, 'mine'] in full_grid:
                adjacent_mines += 1
            if [x + 1, y + 1, 'mine'] in full_grid:
                adjacent_mines += 1

            full_grid[i][2] = str(adjacent_mines)

    for i in range(0, len(full_grid)):  # generate squares into group for blit
        x = full_grid[i][0]
        y = full_grid[i][1]
        z = full_grid[i][2]
        if z != 'wall':
            square = Squares(square_plus2 * x + 1, square_plus2 * y + 1, z)
            bottom_square_group.add(square)


def createCoverTiles():
    top_grid = []
    for i in range(1, columns + 1):  # generating tiles to cover lower grid
        for j in range(1, rows + 1):
            top_grid.append([i, j, 'top'])

    for i in range(0, columns * rows):  # generate squares into group for blit for j in range(1, rows + 1):
        x = top_grid[i][0]
        y = top_grid[i][1]
        z = top_grid[i][2]

        square = Squares(square_plus2 * x + 1, square_plus2 * y + 1, z)
        cover_tiles_group.add(square)


def createMouseSprite():
    mouse = Mouse(15, 15)
    mouse_group.add(mouse)
