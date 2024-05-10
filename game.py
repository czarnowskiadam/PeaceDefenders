from imports import *
from button import Button
from animator import *
from transition import *
from text_render import *

pygame.display.init()
pygame.font.init()

is_fullscreen = False

resolutions = [(1920, 1080), (1600, 900), (1536, 864), (1366,768), (1280, 720), (1024, 576)]
WINDOW_SIZE = None
monitor_width, monitor_height = pygame.display.Info().current_w, pygame.display.Info().current_h
monitor_resolution = (monitor_width, monitor_height)

if monitor_resolution in resolutions:
    WINDOW_SIZE = monitor_resolution
    if WINDOW_SIZE == resolutions[0] and not is_fullscreen:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (0, 10)
else:
    WINDOW_SIZE = min(resolutions)




possible_fps = [30, 60, 90, 120, 144]
FPS = 60

font_size_18 = 18
font = pygame.font.Font("font/daydream.ttf", font_size_18)
options_stats_button_font_size_20 = 20
small_options_stats_font_size = 26

bg = pygame.image.load("assets/background/bg.png")
logo_sprite = pygame.image.load("assets/logo/logo.png")
frame_width, frame_height = 900, 300
options_stats_menu_image = pygame.image.load("assets/menu/options_stats.png")
button_image_on_path = 'assets/buttons/button208x48xON.png'
button_image_off_path = 'assets/buttons/button208x48xOFF1.png'
button_on_image = pygame.image.load(button_image_on_path)
button_off_image = pygame.image.load(button_image_off_path)

logo_pos = [480, 550]
start_text_pos = [775, 800]

start_button_pos = (856, 600)
options_button_pos = (856, 680)
stats_button_pos = (856, 760)
quit_button_pos = (856, 840)

options_menu_pos = (240, 135)
options_text_pos = [int(WINDOW_SIZE[0] / 2), 210]
video_settings_button_pos = (460, 280)
audio_settings_button_pos = (720, 280)
keys_settings_button_pos = (980, 280)
back_settings_button_pos = (1240, 280)

stats_menu_pos = (240, 135)
stats_text_pos = [int(WINDOW_SIZE[0] / 2), 210]

fps_text_pos = (820, 420)
fps_button_pos = (980, 400)

resolution_text_pos = (820, 500)
resolution_button_pos = (980, 480)

fullscreen_text_pos = (820, 580)
fullscreen_button_pos = (980, 560)


def scale_features():
    global bg, logo_pos, start_text_pos, logo_sprite, frame_width, frame_height, font, font_size_18
    global start_button_pos, options_button_pos, stats_button_pos, quit_button_pos, button_on_image, button_off_image
    global options_stats_menu_image, options_menu_pos, options_text_pos, video_settings_button_pos, audio_settings_button_pos, keys_settings_button_pos, back_settings_button_pos
    global options_stats_button_font_size_20, stats_menu_pos, stats_text_pos
    global fps_text_pos, fps_button_pos, small_options_stats_font_size, resolution_text_pos, resolution_button_pos, fullscreen_text_pos, fullscreen_button_pos

    scale_factor = WINDOW_SIZE[0] / 1920

    bg = pygame.transform.scale(bg, (int(bg.get_width() * scale_factor), int(bg.get_height() * scale_factor)))
    frame_width, frame_height = int(frame_width * scale_factor), int(frame_height * scale_factor)
    logo_sprite = pygame.transform.scale(logo_sprite, (int(logo_sprite.get_width() * scale_factor), int(logo_sprite.get_height() * scale_factor)))
    logo_pos = (int(logo_pos[0] * scale_factor), int(logo_pos[1] * scale_factor))
    font_size_18 = int(font_size_18 * scale_factor)
    font = pygame.font.Font("font/daydream.ttf", font_size_18)
    start_text_pos = (int(start_text_pos[0] * scale_factor), int(start_text_pos[1] * scale_factor))

    button_on_image = pygame.transform.scale(button_on_image, (int(button_on_image.get_width() * scale_factor), int(button_on_image.get_height() * scale_factor)))
    button_off_image = pygame.transform.scale(button_off_image, (int(button_off_image.get_width() * scale_factor), int(button_off_image.get_height() * scale_factor)))
    start_button_pos = (int(start_button_pos[0] * scale_factor), int(start_button_pos[1] * scale_factor))
    options_button_pos = (int(options_button_pos[0] * scale_factor), int(options_button_pos[1] * scale_factor))
    stats_button_pos = (int(stats_button_pos[0] * scale_factor), int(stats_button_pos[1] * scale_factor))
    quit_button_pos = (int(quit_button_pos[0] * scale_factor), int(quit_button_pos[1] * scale_factor))

    options_stats_button_font_size_20 = int(options_stats_button_font_size_20 * scale_factor)

    options_stats_menu_image = pygame.transform.scale(options_stats_menu_image, (int(options_stats_menu_image.get_width() * scale_factor), int(options_stats_menu_image.get_height() * scale_factor)))
    options_menu_pos = (int(options_menu_pos[0] * scale_factor), int(options_menu_pos[1] * scale_factor))
    options_text_pos[1] = int(options_text_pos[1] * scale_factor)
    video_settings_button_pos = (int(video_settings_button_pos[0] * scale_factor), int(video_settings_button_pos[1] * scale_factor))
    audio_settings_button_pos = (int(audio_settings_button_pos[0] * scale_factor), int(audio_settings_button_pos[1] * scale_factor))
    keys_settings_button_pos = (int(keys_settings_button_pos[0] * scale_factor), int(keys_settings_button_pos[1] * scale_factor)) 
    back_settings_button_pos = (int(back_settings_button_pos[0] * scale_factor), int(back_settings_button_pos[1] * scale_factor))        

    stats_menu_pos = (int(stats_menu_pos[0] * scale_factor), int(stats_menu_pos[1] * scale_factor))
    stats_text_pos[1] = int(stats_text_pos[1] * scale_factor)     

    small_options_stats_font_size = int(small_options_stats_font_size * scale_factor)
    fps_text_pos = (int(fps_text_pos[0] * scale_factor), int(fps_text_pos[1] * scale_factor)) 
    fps_button_pos = (int(fps_button_pos[0] * scale_factor), int(fps_button_pos[1] * scale_factor))

    resolution_text_pos = (int(resolution_text_pos[0] * scale_factor), int(resolution_text_pos[1] * scale_factor))
    resolution_button_pos = (int(resolution_button_pos[0] * scale_factor), int(resolution_button_pos[1] * scale_factor))

    fullscreen_text_pos = (int(fullscreen_text_pos[0] * scale_factor), int(fullscreen_text_pos[1] * scale_factor))
    fullscreen_button_pos = (int(fullscreen_button_pos[0] * scale_factor), int(fullscreen_button_pos[1] * scale_factor))

def reset_features_scale():
    global bg, logo_pos, start_text_pos, logo_sprite, frame_width, frame_height, font, font_size_18
    global start_button_pos, options_button_pos, stats_button_pos, quit_button_pos, button_on_image, button_off_image
    global options_stats_menu_image, options_menu_pos, options_text_pos, video_settings_button_pos, audio_settings_button_pos, keys_settings_button_pos, back_settings_button_pos
    global options_stats_button_font_size_20, stats_menu_pos, stats_text_pos
    global fps_text_pos, fps_button_pos, small_options_stats_font_size, resolution_text_pos, resolution_button_pos, fullscreen_text_pos, fullscreen_button_pos
    font_size_18 = 18
    font = pygame.font.Font("font/daydream.ttf", font_size_18)
    options_stats_button_font_size_20 = 20
    small_options_stats_font_size = 26

    bg = pygame.image.load("assets/background/bg.png")
    logo_sprite = pygame.image.load("assets/logo/logo.png")
    frame_width, frame_height = 900, 300
    options_stats_menu_image = pygame.image.load("assets/menu/options_stats.png")
    button_image_on_path = 'assets/buttons/button208x48xON.png'
    button_image_off_path = 'assets/buttons/button208x48xOFF.png'
    button_on_image = pygame.image.load(button_image_on_path)
    button_off_image = pygame.image.load(button_image_off_path)

    logo_pos = [480, 550]
    start_text_pos = [775, 800]

    start_button_pos = (856, 600)
    options_button_pos = (856, 680)
    stats_button_pos = (856, 760)
    quit_button_pos = (856, 840)

    options_menu_pos = (240, 135)
    options_text_pos = [int(WINDOW_SIZE[0] / 2), 210]
    video_settings_button_pos = (460, 280)
    audio_settings_button_pos = (720, 280)
    keys_settings_button_pos = (980, 280)
    back_settings_button_pos = (1240, 280)

    stats_menu_pos = (240, 135)
    stats_text_pos = [int(WINDOW_SIZE[0] / 2), 210]

    fps_text_pos = (820, 420)
    fps_button_pos = (980, 400)

    resolution_text_pos = (820, 500)
    resolution_button_pos = (980, 480)

    fullscreen_text_pos = (820, 580)
    fullscreen_button_pos = (980, 560)

def begining_screen(window, clock, FPS):
    frames, total_frames, frame_index, frame_countdown = animate_sprites(logo_sprite, frame_width, frame_height, 1, 8)    

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

        frame_index, frame_countdown = update_sprites(window, frames, total_frames, frame_index, frame_countdown, logo_pos)
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
        start_text_rect = start_text.get_rect(topleft=start_text_pos)
        window.blit(start_text, start_text_rect)

        pygame.display.update()
        clock.tick(FPS)

def main_menu(window, clock, FPS):
    click = False

    fade_alpha = 255

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
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False 

        start_button = Button(window, start_button_pos, button_on_image, button_off_image, 'START', options_stats_button_font_size_20, (255, 255, 255))
        options_button = Button(window, options_button_pos, button_on_image, button_off_image, 'OPTIONS', options_stats_button_font_size_20, (255, 255, 255))
        statistics_button = Button(window, stats_button_pos, button_on_image, button_off_image, 'STATS', options_stats_button_font_size_20, (255, 255, 255))
        quit_button = Button(window, quit_button_pos, button_on_image, button_off_image, 'QUIT', options_stats_button_font_size_20, (255, 255, 255))
        if start_button.click(click):
            start_button.draw()
            fade_alpha = 255
            start(window, clock, FPS)
            click = False
        if options_button.click(click):
            options_button.draw()
            fade_alpha = 255
            options_menu(window, clock, FPS)
            click = False
        if statistics_button.click(click):
            statistics_button.draw()
            fade_alpha = 255
            stats_menu(window, clock, FPS)
            click = False
        if quit_button.click(click):
            quit_button.draw()
            pygame.quit()
            sys.exit()

        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        pygame.display.update()
        clock.tick(FPS)

def options_menu(window, clock, fps):
    global WINDOW_SIZE, is_fullscreen, FPS

    fps_index = possible_fps.index(FPS)
    res_index = resolutions.index(WINDOW_SIZE)

    click = False
    fade_alpha = 255

    settings_choices = ["video", "audio", "keys"]
    current_choice = settings_choices[0]

    running = True
    while running:
        window.blit(bg, (0, 0))
        window.blit(options_stats_menu_image, options_menu_pos)

        fs = None
        if not is_fullscreen:
            fs = 'OFF'
        else:
            fs = 'ON'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False 

        display_text(window, "OPTIONS", small_options_stats_font_size, options_text_pos, (255, 255, 255))

        video_settings_button = Button(window, video_settings_button_pos, button_on_image, button_off_image, 'VIDEO', options_stats_button_font_size_20, (255, 255, 255))
        audio_settings_button = Button(window, audio_settings_button_pos, button_on_image, button_off_image, 'AUDIO', options_stats_button_font_size_20, (255, 255, 255))
        keys_settings_button = Button(window, keys_settings_button_pos, button_on_image, button_off_image, 'BIND KEYS', options_stats_button_font_size_20, (255, 255, 255))
        back_settings_button = Button(window, back_settings_button_pos, button_on_image, button_off_image, 'BACK', options_stats_button_font_size_20, (255, 255, 255))

        if video_settings_button.click(click):
            video_settings_button.draw()
            current_choice = settings_choices[0]
            click = False
        if audio_settings_button.click(click):
            audio_settings_button.draw()
            current_choice = settings_choices[1]
            click = False
        if keys_settings_button.click(click):
            keys_settings_button.draw()
            current_choice = settings_choices[2]
            click = False
        if back_settings_button.click(click):
            back_settings_button.draw()
            running = False
            click = False

        if current_choice == 'video':
            
            display_text(window, "FPS", small_options_stats_font_size, fps_text_pos, (255, 255, 255))
            fps_button = Button(window, fps_button_pos, button_on_image, button_off_image, f"{FPS}", options_stats_button_font_size_20, (255, 255, 255))
            if fps_button.click(click):
                fps_button.draw()
                if fps_index == len(possible_fps) - 1:
                    fps_index = 0
                else:
                    fps_index += 1
                FPS = possible_fps[fps_index]
                click = False

            display_text(window, "Resolution", small_options_stats_font_size, resolution_text_pos, (255, 255, 255))
            resolutin_button = Button(window, resolution_button_pos, button_on_image, button_off_image, f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}", options_stats_button_font_size_20, (255, 255, 255))
            if resolutin_button.click(click):
                resolutin_button.draw()
                if res_index == len(resolutions) - 1:
                    res_index = 0
                    WINDOW_SIZE = resolutions[res_index]
                else:
                    res_index += 1
                    WINDOW_SIZE = resolutions[res_index]

                if is_fullscreen:
                    window = pygame.display.set_mode((monitor_width, monitor_height), pygame.FULLSCREEN)
                    reset_features_scale()
                    scale_features()
                else:
                    window = pygame.display.set_mode(WINDOW_SIZE)
                    reset_features_scale()
                    scale_features()
                click = False
            


            display_text(window, "Fullscreen", small_options_stats_font_size, fullscreen_text_pos, (255, 255, 255))
            fullscreen_button = Button(window, fullscreen_button_pos, button_on_image, button_off_image, f"{fs}", options_stats_button_font_size_20, (255, 255, 255))
            if fullscreen_button.click(click):
                fullscreen_button.draw()
                if not is_fullscreen:
                    is_fullscreen = True
                    window = pygame.display.set_mode((monitor_width, monitor_height), pygame.FULLSCREEN)
                else:
                    is_fullscreen = False
                    window = pygame.display.set_mode(WINDOW_SIZE)
                click = False

        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        pygame.display.update()
        clock.tick(fps) 

def stats_menu(window, clock, FPS):
    click = False
    fade_alpha = 255

    running = True
    while running:
        window.blit(bg, (0, 0))
        window.blit(options_stats_menu_image, stats_menu_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        display_text(window, "STATS", 26, stats_text_pos, (255, 255, 255))

        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        pygame.display.update()
        clock.tick(FPS) 

def start(window, clock, FPS):
    click = False
    fade_alpha = 255

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
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False  
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        _, fade_alpha = fade_in_surface(window, fade_alpha, 5)

        pygame.display.update()
        clock.tick(FPS) 


class GameWindow(object):
    def __init__(self):        
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        scale_features()

        self.game_clock = pygame.time.Clock()

        self.WINDOW_TITLE = "Tower Defense"
        pygame.display.set_caption(self.WINDOW_TITLE)


        self.window_loop()
       

    def window_loop(self):
        begining_screen(self.window, self.game_clock, FPS)      

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()         


GameWindow()