from imports import *

def display_text(window, text, font_size, position, color):
    font = pygame.font.Font("font/daydream.ttf", font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    window.blit(text_surface, text_rect)