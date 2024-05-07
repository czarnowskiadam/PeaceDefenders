from imports import *

def fade_in_surface(surface, fade_alpha, fade_speed):

    fade_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    fade_surface.fill((0, 0, 0, fade_alpha))
    surface.blit(fade_surface, (0, 0))

    if fade_alpha > 0:
        fade_alpha = max(0, fade_alpha - fade_speed)
        return True, fade_alpha
    else:
        return False, fade_alpha
    
