import pygame
from pygame import draw

    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.flip()
    for i in range(3):
        pygame.draw.rect(screen, (255, 255, 255), (751, 409 + i * 150, 422, 100), 5, 20)
    name = pygame.font.SysFont(None, 200).render('Just Survive', False,
                  (255, 255, 255))
    screen.blit(name, (555, 76))

    start_btn = pygame.font.SysFont(None, 128).render("Start", False,
                  (255, 255, 255))
    screen.blit(start_btn, (851, 421))

    res_btn = pygame.font.SysFont(None, 128).render("Results", False,
                  (255, 255, 255))
    screen.blit(res_btn, (799, 571))

    quit_btn = pygame.font.SysFont(None, 128).render("Quit", False,
                  (255, 255, 255))
    screen.blit(quit_btn, (867, 721))

    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    
