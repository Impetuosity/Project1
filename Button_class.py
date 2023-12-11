import pygame

class Button:
    def __init__(self, x, y, width, height, color, text, s, border_radius, text_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont(None, text_size)
        self.s = s
        self.br = border_radius

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.s, border_radius=self.br)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        if (self.x < mouse_pos[0] < self.x + self.width) and (self.y < mouse_pos[1] < self.y + self.height):
            return True
        else:
            return False
