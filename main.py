import pygame
import math
import random

RADIUS = 35
FPS = 120


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(enemies)
        self.lifetime = 3
        self.add(enemies)
        self.add(all_sprites)
        self.image = pygame.Surface((2 * RADIUS, 2 * RADIUS),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        side = random.randint(0, 3)
        if side == 0:
            self.rect.x = random.randint(1, 1920)
            self.rect.y = 1
            self.y_s = random.randint(-1, 1)
            self.x_s = 2
        elif side == 1:
            self.rect.x = 1
            self.rect.y = random.randint(1, 1080)
            self.y_s = random.randint(-1, 1)
            self.x_s = 2
        elif side == 2:
            self.rect.x = 1920 - RADIUS
            self.rect.y = random.randint(1, 1080)
            self.y_s = random.randint(-1, 1)
            self.x_s = -2
        elif side == 3:
            self.rect.x = random.randint(1, 1920)
            self.rect.y = 1080 - RADIUS
            self.y_s = -2
            self.x_s = random.randint(-1, 1)

    def update(self):
        if self.lifetime < 0:
            self.kill()
        self.rect = self.rect.move(self.x_s, self.y_s)
        self.rect = self.rect.move(self.x_s, self.y_s)
        if pygame.sprite.spritecollideany(self, horizontal):
            self.y_s = -self.y_s
            self.lifetime -= 1
        if pygame.sprite.spritecollideany(self, vertical):
            self.x_s = -self.x_s
            self.lifetime -= 1



class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(enemies)
        if x1 == x2:
            self.add(vertical)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.pos = (1920 // 2, 1080 // 2)
        self.radius = 35
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("black"),
                           (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.image, pygame.Color('white'), (self.radius, self.radius), self.radius * 0.47)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.player_speed = 9

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
horizontal = pygame.sprite.Group()
vertical = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
Border(0, 0, 1920, 0)
Border(0, 1080, 1920, 1080)
Border(0, 0, 0, 1080)
Border(1920, 0, 1920, 1080)
player = Player()
all_sprites.add(player)



def Circal_dvd():
    for i in range(2):
        Enemies()


def play():
    collor = pygame.Color('blue')
    if __name__ == '__main__':
        time = 0
        mouse_cursor = pygame.Surface((35 * 2, 35 * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(mouse_cursor, pygame.Color("black"),
                           (35, 35), 35, 3)
        X = 1920
        Y = 1080
        screen = pygame.display.set_mode((X, Y))
        screen.fill(collor)
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
            time += 1
            if (time / FPS) % 15 == 0:
                print('spawn')
                Circal_dvd()
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse_cursor, (x - 35, y - 35))
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            screen.fill(collor)
        clock.tick(120)
    pygame.quit()


play()
