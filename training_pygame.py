import pygame
import sys

# Каркас игры на Pygame
# pygame.init()
# pygame.display.set_mode((600,400))

# FPS = 60

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     clock.tick(FPS)

# Задание

# pygame.init()
# pygame.display.set_mode((600,400))

# FPS = 60

# clock = pygame.time.Clock()

# while True:
#     pygame.display.set_caption('Pygame')
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     clock.tick(FPS)

# Модуль pygame.draw

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     surface_main.fill(WHITE)
#     pygame.draw.circle(surface_main, ORANGE, (x,y), r)
#     pygame.display.update()
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# Задание

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     surface_main.fill(WHITE)
#     pygame.draw.rect(surface_main, ORANGE, (x, y, r, r))
#     pygame.display.update()
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# События клавиатуры

# pygame.init()

# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# WIN_WIDTH = 400
# WIN_HEIGHT = 100

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

# clock = pygame.time.Clock()

# r = 30
# x = 0 - r
# y = WIN_HEIGHT // 2

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif i.type == pygame.KEYUP:
#             reverse_move = True
#     surface_main.fill(WHITE)
#     pygame.draw.rect(surface_main, ORANGE, (x, y, r, r))
#     pygame.display.update()
#     if x > 0 and reverse_move:
#         x -= 4
#     elif x <= 0:
#         reverse_move = False
#     if x >= WIN_WIDTH + r:
#         x = 0 - r
#     else:
#         x += 2
#     clock.tick(FPS)

# События мыши

# pygame.init()

# WIDTH = 600
# HEIGHT = 400
# FPS = 60
# MOVING_CIRCLE = False
# y = 400
# y_mouse = 0
# BOOM = False
# WHITE = (255,255,255)
# ORANGE = (255, 150, 100)
# BOOM_RESULT = False

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif i.type == pygame.MOUSEBUTTONDOWN:
#             y_mouse = pygame.mouse.get_pos()[1]
#             MOVING_CIRCLE = True

#     if MOVING_CIRCLE and BOOM_RESULT:
#         y = 400
#         BOOM = False
#         BOOM_RESULT = False

#     surface_main.fill(WHITE)
#     if not BOOM:
#         pygame.draw.circle(surface_main, ORANGE, (300, y), 10)
#     else:
#         pygame.draw.rect(surface_main, ORANGE, (290, y-10, 20, 20))
#         BOOM_RESULT = True
#     pygame.display.update()
     
#     if MOVING_CIRCLE and y > y_mouse:
#         y -= 2
#     elif MOVING_CIRCLE and y <= y_mouse:
#         MOVING_CIRCLE = False
#         BOOM = True

#     clock.tick(FPS)

# Класс Surface и метод blit()

# pygame.init()

# WIDTH = 600
# HEIGHT = 400
# FPS = 60
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# x = 0

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# surface_main.fill(WHITE)

# surface_2 = pygame.Surface((WIDTH / 6, HEIGHT))
# surface_2.fill(WHITE)

# pygame.draw.rect(surface_2, ORANGE, (10,10, 80, 80))
# pygame.draw.circle(surface_2, ORANGE, (50, 150), 40)
# pygame.draw.polygon(surface_2, ORANGE, ((50, 210), (90, 270), (10, 270)))

# surface_main.blit(surface_2, (x,0))

# pygame.display.update()

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
    
#     if x > 600:
#         x = -90

#     surface_main.blit(surface_2, (x,0))

#     pygame.display.update()

#     x += 1
    
#     clock.tick(FPS)

# Класс Rect

# pygame.init()

# FPS = 60
# WIDTH = 600
# HEIGHT = 400
# WHITE = (255,255,255)
# ORANGE = (255,150,100)
# YELLOW = (255,200,0)
# mouse_color = False

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# surface_1 = pygame.Surface((WIDTH // 2, HEIGHT // 2))
# surface_2 = pygame.Surface((WIDTH // 2, HEIGHT // 2))
# surface_3 = pygame.Surface((WIDTH // 2, HEIGHT // 2))
# surface_4 = pygame.Surface((WIDTH // 2, HEIGHT // 2))

# surface_1.fill(WHITE)
# surface_2.fill(WHITE)
# surface_3.fill(WHITE)
# surface_4.fill(WHITE)

# rect_1 = pygame.Rect(0,0, WIDTH // 2, HEIGHT // 2)
# rect_2 = pygame.Rect(WIDTH // 2, 0, WIDTH // 2, HEIGHT // 2)
# rect_3 = pygame.Rect(0, HEIGHT // 2, WIDTH // 2, HEIGHT // 2)
# rect_4 = pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2)

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif i.type == pygame.MOUSEBUTTONDOWN:
#             if mouse_color == True:
#                 mouse_color = False
#             else:
#                 mouse_color = True

#     if mouse_color == True:
#         pygame.draw.circle(surface_1, ORANGE, (WIDTH // 2, HEIGHT // 2), 150)
#         pygame.draw.circle(surface_2, YELLOW, (0, HEIGHT // 2), 150)
#         pygame.draw.circle(surface_3, YELLOW, (WIDTH // 2, 0), 150)
#         pygame.draw.circle(surface_4, ORANGE, (0, 0), 150)
#     else:
#         pygame.draw.circle(surface_1, YELLOW, (WIDTH // 2, HEIGHT // 2), 150)
#         pygame.draw.circle(surface_2, ORANGE, (0, HEIGHT // 2), 150)
#         pygame.draw.circle(surface_3, ORANGE, (WIDTH // 2, 0), 150)
#         pygame.draw.circle(surface_4, YELLOW, (0, 0), 150)

#     surface_main.blit(surface_1, rect_1)
#     surface_main.blit(surface_2, rect_2)
#     surface_main.blit(surface_3, rect_3)
#     surface_main.blit(surface_4, rect_4)

#     pygame.display.update(rect_1)
#     pygame.display.update(rect_2)
#     pygame.display.update(rect_3)
#     pygame.display.update(rect_4)

    # clock.tick(FPS)

# Модуль pygame.font

# pygame.init()

# FPS = 60
# WIDTH = 600
# HEIGHT = 400
# WHITE = (255, 255, 255)
# ORANGE = (255,150,100)
# BLUE = (0, 77, 255)
# GREEN = (0, 100, 0)
# x = WIDTH // 2 - 25
# y = HEIGHT // 2 - 25


# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# surface_1 = pygame.Surface((50,50))
# surface_2 = pygame.Surface((100,100))

# rect_1 = pygame.Rect(x, y, 50, 50)
# rect_2 = pygame.Rect(x-25, y-25, 100, 100)

# surface_main.fill(WHITE)

# rectangle_1 = pygame.draw.rect(surface_1, ORANGE, (0, 0, 50, 50))
# rectangle_2 = pygame.draw.rect(surface_2, BLUE, (0, 0, 100, 100))

# font = pygame.font.Font(None, 72)
# text_1 = font.render('True', True, GREEN)
# text_2 = font.render('False', True, GREEN)
# place_1 = text_1.get_rect(center=(WIDTH // 2, HEIGHT - 100))
# place_2 = text_2.get_rect(center=(WIDTH // 2, HEIGHT - 100))

# surface_main.blit(surface_1, rect_1)
# surface_main.blit(surface_2, rect_2)

# pygame.display.update()

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
#         elif i.type == pygame.MOUSEBUTTONDOWN:
#             x, y = i.pos[0], i.pos[1]
#             rect_1.x, rect_1.y = x-25, y-25
    
#     surface_main.fill(WHITE)

#     surface_main.blit(surface_2, rect_2)
#     surface_main.blit(surface_1, rect_1)
#     if rect_2.contains(rect_1):
#         surface_main.blit(text_1, place_1)
#     else:
#         surface_main.blit(text_2, place_2)

#     pygame.display.update()

    # clock.tick(FPS)

# Модули pygame.image и pygame.transform

# pygame.init()

# FPS = 60
# WIDTH = 600
# HEIGHT = 400
# WHITE = (255,255,255)
# x = WIDTH // 2
# y = HEIGHT // 2

# pygame.display.set_caption('Pygame')
# surface_main = pygame.display.set_mode((WIDTH, HEIGHT))

# surface_main.fill(WHITE)

# img_car = pygame.image.load('img/car.png').convert_alpha()
# place_car = img_car.get_rect(center=(x,y))

# scale = pygame.transform.scale(img_car, (img_car.get_width() // 4, img_car.get_height() // 4))
# scale_rect = scale.get_rect(center=(x,y))

# surface_main.blit(scale, scale_rect)

# clock = pygame.time.Clock()

# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
#         elif i.type == pygame.KEYDOWN:
#             if i.key == pygame.K_UP:
#                 y -= 10
#                 surface_main.fill(WHITE)
#                 scale = pygame.transform.scale(img_car, (img_car.get_width() // 4, img_car.get_height() // 4))
#                 scale_rect = scale.get_rect(center=(x,y))

#                 surface_main.blit(scale, scale_rect)
#             elif i.key == pygame.K_LEFT:
#                 x -= 10
#                 surface_main.fill(WHITE)
#                 scale = pygame.transform.scale(img_car, (img_car.get_width() // 4, img_car.get_height() // 4))
#                 rot = pygame.transform.rotate(scale, 90)
#                 rot_rect = rot.get_rect(center=(x,y))

#                 surface_main.blit(rot, rot_rect)
#             elif i.key == pygame.K_RIGHT:
#                 x += 10
#                 surface_main.fill(WHITE)
#                 scale = pygame.transform.scale(img_car, (img_car.get_width() // 4, img_car.get_height() // 4))
#                 rot = pygame.transform.rotate(scale, 270)
#                 rot_rect = rot.get_rect(center=(x,y))

#                 surface_main.blit(rot, rot_rect)
#             elif i.key == pygame.K_DOWN:
#                 y += 10
#                 surface_main.fill(WHITE)
#                 scale = pygame.transform.scale(img_car, (img_car.get_width() // 4, img_car.get_height() // 4))
#                 rot = pygame.transform.rotate(scale, 180)
#                 rot_rect = rot.get_rect(center=(x,y))

#                 surface_main.blit(rot, rot_rect)

#     pygame.display.update()

#     clock.tick(FPS)