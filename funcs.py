from cfg import *


def deleteFromTopGrid(x, y):
    for i in top_grid:
        if x == i[0] and y == i[1]:
            top_grid.remove(i)
    for j in full_grid:
        if x == j[0] and y == j[1] and j[2] == '0':
            cover = [x, y, 'top']
            covers_of_zeros.append(cover)


def convertPixelsToRowCols(x, y):
    x = int((x - 1) / square_plus2)
    y = int((y - 1) / square_plus2)
    return x, y


def convertRowColsToPixels(x, y):
    x = square_plus2 * x + 1
    y = square_plus2 * y + 1
    return x, y


def ClearSurroundingEmptyTiles(x, y):

    surrounding_tiles = [[x - 1, y - 1],
                         [x - 1, y],
                         [x - 1, y + 1],
                         [x, y - 1],
                         [x, y + 1],
                         [x + 1, y - 1],
                         [x + 1, y],
                         [x + 1, y + 1]]

    for tile in surrounding_tiles:
        a = tile[0]
        b = tile[1]
        top_tile = [a, b, 'top']
        bottom_tile = [a, b, '0']

        if top_tile in top_grid and bottom_tile in full_grid:
            top_grid.remove(top_tile)
            covers_of_zeros.append(top_tile)
            ClearSurroundingEmptyTiles(a, b)


def ClearNumberedTiles():

    surrounding_tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for tile in covers_of_zeros:
        x = tile[0]
        y = tile[1]

        surrounding_tiles[1] = [x - 1, y - 1, 'top']
        surrounding_tiles[2] = [x - 1, y, 'top']
        surrounding_tiles[3] = [x - 1, y + 1, 'top']
        surrounding_tiles[4] = [x, y - 1, 'top']
        surrounding_tiles[5] = [x, y + 1, 'top']
        surrounding_tiles[6] = [x + 1, y - 1, 'top']
        surrounding_tiles[7] = [x + 1, y, 'top']
        surrounding_tiles[8] = [x + 1, y + 1, 'top']

        for i in range(1, 9):
            if surrounding_tiles[i] in top_grid:
                top_grid.remove(surrounding_tiles[i])
