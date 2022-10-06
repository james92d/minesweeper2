from cfg import *

from preparation import drawBackground
from preparation import createCoverTiles
from preparation import createGrid
from preparation import createMouseSprite

from mouse import Mouse


createGrid()
createCoverTiles()
createMouseSprite()


def main():

    run = True

    while run:

        pygame.time.Clock().tick(fps)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        drawBackground()
        bottom_square_group.draw(window)
        cover_tiles_group.update()
        cover_tiles_group.draw(window)
        mouse_group.update()
        # mouse_group.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    main()

