from imports import *

class Button(object):
    def __init__(self, screen, position, button_on_image, button_off_image, text, text_size, text_color):

        self.screen = screen
        self.position = position
        self.button_on_image = button_on_image
        self.button_off_image = button_off_image
        self.current_image = self.button_on_image
        self.text = text
        self.font = pygame.font.Font('font/daydream.ttf', text_size)
        self.text_color = text_color

        self.draw()

    def draw(self):

        self.screen.blit(self.current_image, self.position)
        button_text = pygame.font.Font.render(self.font, self.text, True, self.text_color)
        text_rect = button_text.get_rect(center=(self.position[0] + self.button_on_image.get_width() / 2,
                                                   self.position[1] + self.button_on_image.get_height() / 2 - 5))
        self.screen.blit(button_text, text_rect)

    def click(self, status):
        mouse_pos = pygame.mouse.get_pos()
        image_rect = self.current_image.get_rect(topleft=self.position)
        if image_rect.collidepoint(mouse_pos) and status:
            self.current_image = self.button_off_image
            return True
        else:
            self.button_off_image = self.button_on_image
            return False