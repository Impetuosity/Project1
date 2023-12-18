import pygame
import lobby
import results

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Game")

current_window = lobby.Window1()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_window.draw(screen)
    next_window = current_window.handle_input(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    if next_window:
        current_window = next_window

    pygame.display.flip()

pygame.quit()