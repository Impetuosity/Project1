import pygame
from pygame import draw

    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.flip()
    pygame.draw.rect(screen, (255, 255, 255), (651, 409, 522, 100), 5, 20)
    f1 = pygame.font.SysFont("Fredoka", 200)
    text1 = f1.render('Just Survive', False,
                  (255, 255, 255))
    f2 = pygame.font.SysFont('Fredoka', 128)
    text2 = f2.render("Start", False,
                  (255, 255, 255))
    screen.blit(text1, (505, 76))
    screen.blit(text2, (701, 421))
    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    
    
