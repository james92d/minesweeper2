from cfg import *
import events

from preparation import drawBackground
from preparation import createOriginalTopGrip
from preparation import createGrid
from preparation import createMouseSprite
from preparation import remakeCoverTilesGroup

createGrid()
createOriginalTopGrip()
createMouseSprite()


def main():
    run = True

    while run:

        pygame.time.Clock().tick(fps)
        events.event_list = pygame.event.get()
        for event in events.event_list:
            if event.type == pygame.QUIT:
                run = False

        drawBackground()
        bottom_square_group.update()
        bottom_square_group.draw(window)
        cover_tiles_group.update()
        bottom_square_group.update()
        remakeCoverTilesGroup()
        cover_tiles_group.draw(window)
        mouse_group.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
