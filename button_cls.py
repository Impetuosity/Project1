import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, s, border_radius, text_size, next_window):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.next_window = next_window
        self.color = color
        self.text_size = text_size
        self.s = s
        self.br = border_radius


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.s, self.br)
        font = pygame.font.SysFont(None, self.text_size)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            return True
        return False

    def get_next_window(self):
        return self.next_window()