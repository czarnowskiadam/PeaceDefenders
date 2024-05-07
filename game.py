from imports import *
from button import Button
from animator import *
from transition import *

pygame.init()


font = pygame.font.Font("font/daydream.ttf", 18)

bg = pygame.image.load("assets/background/bg.png")

def begining_screen(window, clock, FPS):

    logo_sprite = pygame.image.load("assets/logo/logo.png").convert_alpha()
    frames, total_frames, frame_index, frame_countdown = animate_sprites(logo_sprite, 900, 300, 1, 8)

    fade_alpha = 255

    text_alpha = 0
    text_fade_speed = 5
    text_fade_in = True
    start_text = font.render("Press Space to Start", True, (0, 0, 0))

    running = True
    while running:
        window.blit(bg, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main_menu(window, clock, FPS)

        frame_index, frame_countdown = update_sprites(window, frames, total_frames, frame_index, frame_countdown)
        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        
        if text_fade_in:
            text_alpha += text_fade_speed
            if text_alpha >= 255:
                text_alpha = 255
                text_fade_in = False
        else:
            text_alpha -= text_fade_speed
            if text_alpha <= 0:
                text_alpha = 0
                text_fade_in = True

        start_text.set_alpha(text_alpha)
        start_text_rect = start_text.get_rect(topleft=(745, 800))
        window.blit(start_text, start_text_rect)

        pygame.display.update()
        clock.tick(FPS)

def main_menu(window, clock, FPS):
    click = False

    fade_alpha = 255

    button_image_on_path = 'assets/buttons/button208x48xON.png'
    button_image_off_path = 'assets/buttons/button208x48xOFF.png'

    running = True
    while running:
        window.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True   

        start_button = Button(window, (856, 600), button_image_on_path, button_image_off_path, 'START', 20, (255, 255, 255))
        options_button = Button(window, (856, 680), button_image_on_path, button_image_off_path, 'OPTIONS', 20, (255, 255, 255))
        statistics_button = Button(window, (856, 760), button_image_on_path, button_image_off_path, 'STATS', 20, (255, 255, 255))
        quit_button = Button(window, (856, 840), button_image_on_path, button_image_off_path, 'QUIT', 20, (255, 255, 255))
        if start_button.click(click):
            start_button.draw()
            click = False
        if options_button.click(click):
            options_button.draw()
            click = False
        if statistics_button.click(click):
            statistics_button.draw()
            click = False
        if quit_button.click(click):
            quit_button.draw()
            pygame.quit()
            sys.exit()

        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        pygame.display.update()
        clock.tick(FPS)

class GameWindow(object):
    def __init__(self):

        self.WINDOW_SIZE = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.window = pygame.display.set_mode(self.WINDOW_SIZE, pygame.FULLSCREEN)

        self.game_clock = pygame.time.Clock()
        self.FPS = 60 

        self.WINDOW_TITLE = "Tower Defense"
        pygame.display.set_caption(self.WINDOW_TITLE)

        self.window_loop()
       

    def window_loop(self):
        begining_screen(self.window, self.game_clock, self.FPS)      

    def event_loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()         


GameWindow()