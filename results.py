import pygame, lobby
from button_cls import Button

class Window2:
    def __init__(self):
        self.buttons = [Button(100, 100, 200, 50, "Open Window 1", lobby.Window1)]

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 36)
        text = font.render("Window 2", True, (0, 0, 0))
        screen.blit(text, (300, 50))
        for button in self.buttons:
            button.draw(screen)

    def handle_input(self, mouse_pos, mouse_pressed):
        for button in self.buttons:
            if button.is_clicked(mouse_pos, mouse_pressed):
                return button.get_next_window()
        return None