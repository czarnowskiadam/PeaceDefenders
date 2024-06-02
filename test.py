# from imports import *

# user_x, user_y = 1024, 576
# max_x, max_y = 1920, 1080
# bg = pygame.image.load("assets/background/bg.png")

# def begining_screen(window, clock, FPS):
#     surface = pygame.Surface((max_x, max_y)) 

#     running = True
#     while running:
#         surface.blit(bg, (0, 0))
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()

#         window.blit(pygame.transform.scale(surface, window.get_size()), (0, 0))
#         pygame.display.update()
#         clock.tick(FPS)

# class GameWindow(object):
#     def __init__(self):        
#         self.window = pygame.display.set_mode((user_x, user_y))

#         self.game_clock = pygame.time.Clock()

#         self.WINDOW_TITLE = "Tower Defense"
#         pygame.display.set_caption(self.WINDOW_TITLE)


#         self.window_loop()
       

#     def window_loop(self):
#         begining_screen(self.window, self.game_clock, 60)      

#     def event_loop(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     pygame.quit()
#                     sys.exit() 


# GameWindow()

x = (200, 400)
print(x * 2)