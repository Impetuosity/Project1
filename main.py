import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (1920 // 2, 1080 // 2)
        super().__init__(all_sprites)
        self.radius = 10
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (self.radius, self.radius), self.radius)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 2 * self.radius, 2 * self.radius)
        self.player_speed = 1


    def update(self, m_pos):
        dx = m_pos[0] - self.rect.centerx
        dy = m_pos[1] - self.rect.centery
        angle = math.atan2(dy, dx)
        vx = self.player_speed * math.cos(angle)
        vy = self.player_speed * math.sin(angle)
        self.rect = self.rect.move(vx, vy)


class Play:
    def __init__(self):
        self.hard = 1


if __name__ == '__main__':
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
        all_sprites.update(pygame.mouse.get_pos())

