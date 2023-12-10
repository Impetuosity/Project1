import pygame
from pygame import draw


class Button: 
    def __init__(self, x, y, width, height, color, text='',): 
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.color = color 
        self.text = text 
    def draw(self, win, length, border_radius): 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), length, border_radius) 
        if self.text != '': 
            font = pygame.font.SysFont('comicsans', 20) 
            text = font.render(self.text, 1, (0,0,0)) 
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    name = pygame.font.SysFont(None, 200).render('Just Survive', False,
                  (255, 255, 255))
    screen.blit(name, (555, 76))
    button = Button(751, 409 + 0 * 150, 422, 100, (255, 255, 255), '')
    button.draw(screen, 5, 20)
    start_btn = pygame.font.SysFont(None, 128).render("Start", False,
                  (255, 255, 255))
    screen.blit(start_btn, (851, 421))
    button2 = Button(751, 409 + 1 * 150, 422, 100, (255, 255, 255), '')
    button2.draw(screen, 5, 20)
    res_btn = pygame.font.SysFont(None, 128).render("Results", False,
                  (255, 255, 255))
    screen.blit(res_btn, (799, 571))
    button3 = Button(751, 409 + 2 * 150, 422, 100, (255, 255, 255), '')
    button3.draw(screen, 5, 20)
    quit_btn = pygame.font.SysFont(None, 128).render("Quit", False,
                  (255, 255, 255))
    screen.blit(quit_btn, (867, 721))

    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
