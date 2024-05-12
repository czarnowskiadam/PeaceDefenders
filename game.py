from imports import *
from button import Button
from animator import *
from transition import *
from text_render import *
from save import *

pygame.display.init()
pygame.font.init()

is_fullscreen = False

resolutions = [[1920, 1080], [1600, 900], [1536, 864], [1366,768], [1280, 720], [1024, 576]]
max_resolution = max(resolutions)
monitor_info = [pygame.display.Info().current_w, pygame.display.Info().current_h]
monitor_width, monitor_height = 1280, 720
monitor_resolution = [monitor_width, monitor_height]
WINDOW_SIZE = monitor_resolution

if monitor_resolution in resolutions:
    WINDOW_SIZE = monitor_resolution
else:
    WINDOW_SIZE = min(resolutions)

cursor_img = pygame.image.load('assets/cursor/cursor.png')
cursor_width, cursor_height = cursor_img.get_size()
pygame.mouse.set_cursor((0, 0), cursor_img)

possible_fps = [30, 60, 90, 120, 144]
FPS = 60

font_size_18 = 18
font = pygame.font.Font("font/daydream.ttf", font_size_18)
options_stats_button_font_size_20 = 20
small_options_stats_font_size = 26

bg = pygame.image.load("assets/background/bg.png")
options_stats_menu_image = pygame.image.load("assets/menu/options_stats.png")
button_on_image = pygame.image.load('assets/buttons/button208x48xON.png')
button_off_image = pygame.image.load('assets/buttons/button208x48xOFF1.png')

save_path = 'save/save.json'
save = {
    "video_options": {
        "FPS": FPS,
        "resolution": WINDOW_SIZE,
        "is_fullscreen": is_fullscreen
    },
    "audio_options": {
        "volume": 10
    }
}

load = load_save(save_path, save)
if len(load) == 0:
    pass
else:
    FPS = load["video_options"]["FPS"]
    WINDOW_SIZE = load["video_options"]["resolution"]
    is_fullscreen = load["video_options"]["is_fullscreen"]


def beginning_screen(window, dest_surf, clock, FPS):
    logo_sprite = pygame.image.load("assets/logo/logo.png")
    frame_width, frame_height = 900, 300
    logo_pos = [480, 550]
    start_text_pos = [775, 800]

    frames, total_frames, frame_index, frame_countdown = animate_sprites(logo_sprite, frame_width, frame_height, 1, 8)    

    fade_alpha = 255

    text_alpha = 0
    text_fade_speed = 5
    text_fade_in = True
    start_text = font.render("Press Space to Start", True, (0, 0, 0))

    running = True
    while running:
        dest_surf.blit(bg, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    main_menu(window, dest_surf, clock, FPS)

        frame_index, frame_countdown = update_sprites(dest_surf, frames, total_frames, frame_index, frame_countdown, logo_pos)
        _, fade_alpha = fade_in_surface(dest_surf, fade_alpha, 5)

        
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
        dest_surf.blit(start_text, start_text_rect)

        window.blit(pygame.transform.scale(dest_surf, window.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

def main_menu(window, dest_surf, clock, FPS):
    start_button_pos = (856, 600)
    continue_button_pos = (856, 680)
    options_button_pos = (856, 760)
    quit_button_pos = (856, 840)
    click = False

    fade_alpha = 255

    running = True
    while running:
        scale_factor = window.get_width() / dest_surf.get_width()
        dest_surf.blit(bg, (0, 0))

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

        start_button = Button(dest_surf, scale_factor, start_button_pos, button_on_image, button_off_image, 'START', options_stats_button_font_size_20, (255, 255, 255))
        continue_button = Button(dest_surf, scale_factor, continue_button_pos, button_on_image, button_off_image, 'CONTINUE', options_stats_button_font_size_20, (255, 255, 255))
        options_button = Button(dest_surf, scale_factor, options_button_pos, button_on_image, button_off_image, 'OPTIONS', options_stats_button_font_size_20, (255, 255, 255))
        quit_button = Button(dest_surf, scale_factor, quit_button_pos, button_on_image, button_off_image, 'QUIT', options_stats_button_font_size_20, (255, 255, 255))
        if start_button.click(click):
            start_button.draw()
            fade_alpha = 255
            start(window, dest_surf, clock, FPS)
            click = False
        if continue_button.click(click):
            continue_button.draw()
            fade_alpha = 255
            click = False
        if options_button.click(click):
            options_button.draw()
            fade_alpha = 255
            options_menu(window, dest_surf, clock, FPS)
            click = False
        if quit_button.click(click):
            quit_button.draw()
            pygame.quit()
            sys.exit()

        _, fade_alpha = fade_in_surface(dest_surf, fade_alpha, 5)

        window.blit(pygame.transform.scale(dest_surf, window.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(FPS)

def options_menu(window, dest_surf, clock, fps):
    global WINDOW_SIZE, is_fullscreen, FPS

    options_menu_pos = (240, 135)
    options_text_pos = [int(dest_surf.get_width() / 2), 210]
    video_settings_button_pos = (460, 280)
    audio_settings_button_pos = (720, 280)
    keys_settings_button_pos = (980, 280)
    back_settings_button_pos = (1240, 280)

    fps_text_pos = (820, 420)
    fps_button_pos = (980, 400)
    resolution_text_pos = (820, 500)
    resolution_button_pos = (980, 480)
    fullscreen_text_pos = (820, 580)
    fullscreen_button_pos = (980, 560)

    fps_index = possible_fps.index(FPS)
    res_index = resolutions.index(WINDOW_SIZE)

    click = False
    fade_alpha = 255

    settings_choices = ["video", "audio", "keys"]
    current_choice = settings_choices[0]

    running = True
    while running:
        scale_factor = window.get_width() / dest_surf.get_width()
        dest_surf.blit(bg, (0, 0))
        dest_surf.blit(options_stats_menu_image, options_menu_pos)

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

        display_text(dest_surf, "OPTIONS", small_options_stats_font_size, options_text_pos, (255, 255, 255))

        video_settings_button = Button(dest_surf, scale_factor, video_settings_button_pos, button_on_image, button_off_image, 'VIDEO', options_stats_button_font_size_20, (255, 255, 255))
        audio_settings_button = Button(dest_surf, scale_factor, audio_settings_button_pos, button_on_image, button_off_image, 'AUDIO', options_stats_button_font_size_20, (255, 255, 255))
        keys_settings_button = Button(dest_surf, scale_factor, keys_settings_button_pos, button_on_image, button_off_image, 'BIND KEYS', options_stats_button_font_size_20, (255, 255, 255))
        back_settings_button = Button(dest_surf, scale_factor, back_settings_button_pos, button_on_image, button_off_image, 'BACK', options_stats_button_font_size_20, (255, 255, 255))

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
            data = video_options_data()
            write_save(save_path, data)
            running = False
            click = False

        if current_choice == 'video':
            
            display_text(dest_surf, "FPS", small_options_stats_font_size, fps_text_pos, (255, 255, 255))
            fps_button = Button(dest_surf, scale_factor, fps_button_pos, button_on_image, button_off_image, f"{FPS}", options_stats_button_font_size_20, (255, 255, 255))
            if fps_button.click(click):
                fps_button.draw()
                if fps_index == len(possible_fps) - 1:
                    fps_index = 0
                else:
                    fps_index += 1
                FPS = possible_fps[fps_index]
                click = False

            display_text(dest_surf, "Resolution", small_options_stats_font_size, resolution_text_pos, (255, 255, 255))
            resolutin_button = Button(dest_surf, scale_factor, resolution_button_pos, button_on_image, button_off_image, f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}", options_stats_button_font_size_20, (255, 255, 255))
            if resolutin_button.click(click) and not is_fullscreen:
                resolutin_button.draw()
                if is_fullscreen:
                    window = pygame.display.set_mode(monitor_info, pygame.NOFRAME | pygame.FULLSCREEN)
                else:
                    if res_index == len(resolutions) - 1:
                        res_index = 0
                        WINDOW_SIZE = resolutions[res_index]
                    else:
                        res_index += 1
                        WINDOW_SIZE = resolutions[res_index]
                    window = pygame.display.set_mode(WINDOW_SIZE)
                click = False
            
            display_text(dest_surf, "Fullscreen", small_options_stats_font_size, fullscreen_text_pos, (255, 255, 255))
            fullscreen_button = Button(dest_surf, scale_factor, fullscreen_button_pos, button_on_image, button_off_image, f"{fs}", options_stats_button_font_size_20, (255, 255, 255))
            if fullscreen_button.click(click):
                fullscreen_button.draw()
                if not is_fullscreen:
                    is_fullscreen = True
                    window = pygame.display.set_mode(monitor_info, pygame.NOFRAME | pygame.FULLSCREEN)
                    WINDOW_SIZE = monitor_info
                else:
                    is_fullscreen = False
                    window = pygame.display.set_mode(WINDOW_SIZE)
                click = False

        _, fade_alpha = fade_in_surface(dest_surf, fade_alpha, 5)

        window.blit(pygame.transform.scale(dest_surf, window.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(fps)

        def video_options_data():
            save["video_options"]["FPS"] = FPS
            save["video_options"]["resolution"] = WINDOW_SIZE
            save["video_options"]["is_fullscreen"] = is_fullscreen
            return save

def stats_menu(window, dest_surf, clock, FPS):
    stats_menu_pos = (240, 135)
    stats_text_pos = [int(dest_surf.get_width() / 2), 210]
    click = False
    fade_alpha = 255

    running = True
    while running:
        scale_factor = window.get_width() / dest_surf.get_width()
        dest_surf.blit(bg, (0, 0))
        dest_surf.blit(options_stats_menu_image, stats_menu_pos)

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

        display_text(dest_surf, "STATS", 26, stats_text_pos, (255, 255, 255))

        _, fade_alpha = fade_in_surface(dest_surf, fade_alpha, 5)

        window.blit(pygame.transform.scale(dest_surf, window.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(FPS) 

def start(window, dest_surf, clock, FPS):
    click = False
    fade_alpha = 255

    running = True
    while running:
        scale_factor = window.get_width() / dest_surf.get_width()
        dest_surf.blit(bg, (0, 0))

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

        _, fade_alpha = fade_in_surface(dest_surf, fade_alpha, 5)

        window.blit(pygame.transform.scale(dest_surf, window.get_size()), (0, 0))
        pygame.display.update()
        clock.tick(FPS) 

class GameWindow(object):
    def __init__(self):        
        global is_fullscreen, WINDOW_SIZE

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (0, 30)
        if is_fullscreen:
            self.window = pygame.display.set_mode(monitor_info, pygame.NOFRAME | pygame.FULLSCREEN)
            WINDOW_SIZE = monitor_info
        else:
            self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.surface = pygame.Surface(max_resolution)

        self.game_clock = pygame.time.Clock()

        self.WINDOW_TITLE = "Tower Defense"
        pygame.display.set_caption(self.WINDOW_TITLE)


        self.window_loop()
       

    def window_loop(self):
        beginning_screen(self.window, self.surface, self.game_clock, FPS)      

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