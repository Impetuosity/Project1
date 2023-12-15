import pygame
import math

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(enemies)
        self.image = pygame.Surface([1, y2 - y1])
        self.rect = pygame.Rect(x1, y1, 1, y2 - y1)


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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.player_speed = 6

    def update(self):
        if pygame.sprite.spritecollideany(self, enemies):
            print('colides')
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        distance = math.dist((mouse_x, mouse_y), (self.rect.centerx, self.rect.centery))
        if distance >= self.player_speed:
            self.rect.move_ip((self.player_speed * dx) / distance, (self.player_speed * dy) / distance)
        else:
            self.rect.center = pygame.mouse.get_pos()


enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
Border(0, 0, 1920, 0)
Border(0, 1920, 1080, 1920)
Border(0, 0, 0, 1080)
Border(1920, 0, 1920, 1080)
player = Player()
all_sprites.add(player)


def play():
    if __name__ == '__main__':
        mouse_cursor = pygame.Surface((35 * 2, 35 * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(mouse_cursor, pygame.Color("black"),
                           (35, 35), 35, 3)
        X = 1920
        Y = 1080
        screen = pygame.display.set_mode((X, Y))
        screen.fill((255, 255, 255))
        pygame.mouse.set_visible(False)
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
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_cursor, (x - 35, y - 35))
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            screen.fill((255, 255, 255))
        clock.tick(120)
    pygame.quit()


play()
