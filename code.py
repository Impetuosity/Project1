import pygame
from Button_class import Button

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Main menu")

name = pygame.font.SysFont(None, 200).render('Just Survive', False,
                                             (255, 255, 255))
screen.blit(name, (555, 76))

# кнопки
button = Button(751, 409 + 0 * 150, 422, 100, (255, 255, 255), 'Start', 5, 20, 128)
button2 = Button(751, 409 + 1 * 150, 422, 100, (255, 255, 255), 'Results', 5, 20, 128)
button3 = Button(751, 409 + 2 * 150, 422, 100, (255, 255, 255), 'Quit', 5, 20, 128)
#

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.is_clicked(mouse_pos):
                print("Start")
            if button2.is_clicked(mouse_pos):
                print("Results")
            if button3.is_clicked(mouse_pos):
                pygame.quit()
            

    button.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    pygame.display.flip()

pygame.quit()

