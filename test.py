
list = [0, 1, 2, 3, 4, 5]
print(list[2])



# ## squares
#
# import pygame
# import cfg
# from mouse import Mouse
#
#
# class Squares(pygame.sprite.Sprite):
#
#     def __init__(self, x, y, item):
#         pygame.sprite.Sprite.__init__(self)
#           ...

#     def update(self):
#
#         left = (True, False, False)
#         right = (False, False, True)
#         both = (True, False, True)
#
#         mouse_pos = pygame.mouse.get_pos()
#         x_pos = mouse_pos[0]
#         y_pos = mouse_pos[1]
#
#         buttons = pygame.mouse.get_pressed()
#
#         # --- kill cover square and place blocker square ---
#         # if buttons == left and abs(self.rect.x + 15 - x_pos) < 15 and abs(self.rect.y + 15 - y_pos) < 15:
#         #     x = self.rect.x
#         #     y = self.rect.y
#         #     self.kill()
#         #     square = Squares(x, y, '0')
#         #     cfg.cover_tiles_group.add(square)
#
#         # print(cfg.mouse_group)
#
#         collide = pygame.sprite.groupcollide(cfg.cover_tiles_group, cfg.mouse_group, False, False)
#
#         if buttons == left and collide:
#             print('x')
#             x = self.rect.x
#             y = self.rect.y
#             self.kill()
#             square = Squares(x, y, '0')
#             cfg.cover_tiles_group.add(square)
#
#             # for tile in cfg.cover_tiles_group:
#             #     if tile.item == '0' and abs(tile.rect.x + 15 - x_pos) >= 15 and abs(tile.rect.y + 15 - y_pos) >= 15:
#             #         tile.kill()
#
#         # if buttons == left and pygame.sprite.collide_rect(self, mouse_group):
#         #     x = self.rect.x
#         #     y = self.rect.y
#         #     self.kill()
#         #     square = Squares(x, y, '0')
#         #     cover_tiles_group.add(square)
#
#         # # --- kill blocker square and replace cover square ---
#         if buttons != right and buttons != left and buttons != both:
#             for tile in cfg.cover_tiles_group:
#                 if tile.item == '0':
#                     x = tile.rect.x
#                     y = tile.rect.y
#                     tile.kill()
#                     square = Squares(x, y, 'top')
#                     cfg.cover_tiles_group.add(square)
#
#         # if abs(self.rect.x + 15 - x_pos) < 15 and abs(self.rect.y + 15 - y_pos) < 15:
#         #     print('test')
#
#         # for event in events:
#         #     if event.type == pygame.MOUSEBUTTONDOWN:
#         #         if buttons == left and abs(self.rect.x + 15 - x_pos) < 15 and abs(self.rect.y + 15 - y_pos) < 15:
#         #             self.kill()
#
#
#
# left = (True, False, False)
#         right = (False, False, True)
#         both = (True, False, True)
#
#         mouse_pos = pygame.mouse.get_pos()
#         x_pos = mouse_pos[0]
#         y_pos = mouse_pos[1]
#
#         buttons = pygame.mouse.get_pressed()

# collide = pygame.sprite.groupcollide(cfg.cover_tiles_group, cfg.mouse_group, True, True)
#
# print(collide)
#
#
# if collide:
#     print('x')
#     x = self.rect.x
#     y = self.rect.y
#     self.kill()
#     square = Squares(x, y, '0')
#     cfg.cover_tiles_group.add(square)
#
# # # --- kill blocker square and replace cover square ---
# if buttons != right and buttons != left and buttons != both:
#     for tile in cfg.cover_tiles_group:
#         if tile.item == '0':
#             x = tile.rect.x
#             y = tile.rect.y
#             tile.kill()
#             square = Squares(x, y, 'top')
#             cfg.cover_tiles_group.add(square)
