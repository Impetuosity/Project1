import pygame, results, lobby
from button_cls import Button
class Window1:
    def __init__(self):
        self.button_start = Button(751, 409 + 0 * 150, 422, 100, (255, 255, 255), 'Start', 5, 20, 128, results.Window2)
        self.button_result = Button(751, 409 + 1 * 150, 422, 100, (255, 255, 255), 'Results', 5, 20, 128, results.Window2)
        self.button_quit = Button(751, 409 + 2 * 150, 422, 100, (255, 255, 255), 'Quit', 5, 20, 128, results.Window2)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 36)
        text = font.render("Window 1", True, (0, 0, 0))
        screen.blit(text, (300, 50))
        self.button_quit.draw(screen)
        self.button_result.draw(screen)
        self.button_start.draw(screen)

    def handle_input(self, mouse_pos, mouse_pressed):
        for i in range(3):
            if self.button_start.is_clicked(mouse_pos, mouse_pressed):
                return self.button_start.get_next_window()
            elif self.button_result.is_clicked(mouse_pos, mouse_pressed):
                return self.button_result.get_next_window()
            elif self.button_quit.is_clicked(mouse_pos, mouse_pressed):
                pygame.quit()
        return None