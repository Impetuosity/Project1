import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.pos = (1920 // 2, 1080 // 2)
        self.radius = 35
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("black"),
                           (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.player_speed = 5

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        distance = math.dist((mouse_x, mouse_y), (self.rect.centerx, self.rect.centery))
        if distance >= self.player_speed:
            self.rect.move_ip((self.player_speed * dx) / distance, (self.player_speed * dy) / distance)
        else:
            self.rect.center = pygame.mouse.get_pos()

class Play:
    def __init__(self):
        self.hard = 1


if __name__ == '__main__':
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    X = 1920
    Y = 1080
    screen = pygame.display.set_mode((X, Y))
    screen.fill((255, 255, 255))
    pygame.init()
    running = True
    pause = False
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause:
                        pause = False
                    else:
                        pause = True
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((255, 255, 255))
    clock.tick(120)
pygame.quit()
