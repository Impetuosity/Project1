import pygame
import math
import random


pygame.init()
infoObject = pygame.display.Info()
print(infoObject.current_w, infoObject.current_h)
width, height = (infoObject.current_w, infoObject.current_h)
time = 0
pause = True
Size_k = width // 1920
RADIUS = 35 * Size_k
FPS = 120
HARD = 0
pygame.init()
screen = pygame.display.set_mode((width, height))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, x_s, y_s):
        super().__init__(enemies)
        self.lifetime = FPS * 15
        self.add(enemies)
        self.add(all_sprites)
        self.image = pygame.Surface((2 * RADIUS, 2 * RADIUS),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("gray"),
                           (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        if HARD == 0:
            k = 0
        elif HARD == 1:
            k = 1
        elif HARD == 2:
            k = 1
        elif HARD == 3:
            k = 1.5
        elif HARD == 3:
            k = 1.5
        self.y_s = y_s * Size_k
        self.x_s = x_s * Size_k

    def update(self):
        if self.lifetime < 0:
            self.kill()
        self.rect = self.rect.move(self.x_s, self.y_s)
        self.lifetime -= 1


class Enemies_slowly(pygame.sprite.Sprite):
    def __init__(self, x, y, x_s, y_s):
        super().__init__(enemies)
        self.lifetime = FPS * 10
        self.add(enemies)
        self.add(all_sprites)
        self.image = pygame.Surface((2 * RADIUS, 2 * RADIUS),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("green"),
                           (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.y_s = y_s * Size_k
        self.x_s = x_s * Size_k



    def bam(self):
        Bullet(self.rect.x, self.rect.y, -2, -2)
        Bullet(self.rect.x, self.rect.y, 2, 2)
        Bullet(self.rect.x, self.rect.y, -2, 2)
        Bullet(self.rect.x, self.rect.y, 2, -2)
        self.kill()

    def update(self):
        if self.lifetime < 0:
            self.bam()
        if self.lifetime < self.lifetime - FPS * 5:
            self.y_s -= 0.2
            self.x_s -= 0.2
        self.rect = self.rect.move(self.x_s, self.y_s)
        self.lifetime -= 1
        if pygame.sprite.spritecollideany(self, horizontal):
            self.y_s = -self.y_s
            self.lifetime -= 1
        if pygame.sprite.spritecollideany(self, vertical):
            self.x_s = -self.x_s
            self.lifetime -= 1


class Enemies_dvd(pygame.sprite.Sprite):
    def __init__(self, x, y, x_s, y_s):
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
        self.rect.x = x
        self.rect.y = y
        self.y_s = y_s * Size_k
        self.x_s = x_s * Size_k

    def update(self):
        if self.lifetime < 0:
            self.kill()
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
        self.pos = (width // 2, height // 2)
        self.image = pygame.Surface((2 * RADIUS, 2 * RADIUS),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("black"),
                           (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.player_speed = 9 * Size_k

    def update(self):
        for en in enemies:
            offset = (abs(self.rect.x - en.rect.x), abs(self.rect.y - en.rect.y))
            if self.mask.overlap_area(en.mask, offset) > 0:
                print('collides')
                die()
        if pygame.sprite.spritecollideany(self, horizontal):
            print('collides')
            die()
        if pygame.sprite.spritecollideany(self, vertical):
            print('collides')
            die()
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
Border(0, 0, width, 0)
Border(0, height, width, height)
Border(0, 0, 0, height)
Border(width, 0, width, height)
player = Player()
all_sprites.add(player)


def slow():
    if HARD == 0:
        NUM = 0
        SPEED = 0
    elif HARD == 1:
        NUM = 2
        SPEED = 1
    elif HARD == 2:
        NUM = 4
        SPEED = 1
    elif HARD == 3:
        NUM = 6
        SPEED = 1.5
    elif HARD == 4:
        NUM = 10
        SPEED = 1.5
    for i in range(NUM):
        side = random.randint(0, 3)
        if side == 0:
            x = random.choice([RADIUS * 4, width // 2, width - RADIUS * 4])
            y = RADIUS + 1
            y_s = SPEED
            if x == RADIUS * 4:
                x_s = SPEED
            elif x == width - RADIUS * 4:
                x_s = -SPEED
            elif width // 2:
                x_s = random.choice([SPEED, -SPEED])
        elif side == 1:
            x = RADIUS + 1
            y = random.choice([RADIUS * 4, height // 2, height - RADIUS * 4])
            if x == RADIUS * 4:
                y_s = -SPEED
            elif x == height - RADIUS * 4:
                y_s = SPEED
            elif height // 2:
                y_s = random.choice([SPEED, -SPEED])
            x_s = SPEED
        elif side == 2:
            x = width - (RADIUS * 2)
            y = random.choice([RADIUS * 4, height // 2, height - RADIUS * 4])
            if x == RADIUS * 4:
                y_s = SPEED
            elif x == height - RADIUS * 4:
                y_s = -SPEED
            elif height // 2:
                y_s = random.choice([SPEED, -SPEED])
            x_s = -SPEED
        elif side == 3:
            x = random.choice([RADIUS * 4, width // 2, width - RADIUS * 4])
            y = height - (RADIUS * 2)
            y_s = SPEED
            if x == RADIUS * 4:
                x_s = -SPEED
            elif x == width - RADIUS * 4:
                x_s = SPEED
            elif width // 2:
                x_s = random.choice([SPEED, -SPEED])
        Enemies_slowly(x, y, x_s, y_s)

def Circal_dvd():
    if HARD == 0:
        NUM = 0
        SPEED = 0
    elif HARD == 1:
        NUM = 2
        SPEED = 2
    elif HARD == 2:
        NUM = 4
        SPEED = 3
    elif HARD == 3:
        NUM = 6
        SPEED = 4
    elif HARD == 4:
        NUM = 10
        SPEED = 5
    for i in range(NUM):
        side = random.randint(0, 3)
        if side == 0:
            x = random.choice([RADIUS * 4, width // 2, width - RADIUS * 4])
            y = RADIUS + 1
            y_s = SPEED
            if x == RADIUS * 4:
                x_s = SPEED
            elif x == width - RADIUS * 4:
                x_s = -SPEED
            elif width // 2:
                x_s = random.choice([SPEED, -SPEED])
        elif side == 1:
            x = RADIUS + 1
            y = random.choice([RADIUS * 4, height // 2, height - RADIUS * 4])
            if x == RADIUS * 4:
                y_s = -SPEED
            elif x == height - RADIUS * 4:
                y_s = SPEED
            elif height // 2:
                y_s = random.choice([SPEED, -SPEED])
            x_s = SPEED
        elif side == 2:
            x = width - (RADIUS * 2)
            y = random.choice([RADIUS * 4, height // 2, height - RADIUS * 4])
            if x == RADIUS * 4:
                y_s = SPEED
            elif x == height - RADIUS * 4:
                y_s = -SPEED
            elif height // 2:
                y_s = random.choice([SPEED, -SPEED])
            x_s = -SPEED
        elif side == 3:
            x = random.choice([RADIUS * 4, width // 2, width - RADIUS * 4])
            y = height - (RADIUS * 2)
            y_s = SPEED
            if x == RADIUS * 4:
                x_s = -SPEED
            elif x == width - RADIUS * 4:
                x_s = SPEED
            elif width // 2:
                x_s = random.choice([SPEED, -SPEED])
        Enemies_dvd(x, y, x_s, y_s)


def difficulty():
    global HARD
    if time / FPS > 1:
        HARD = 1
    if time / FPS > 60:
        HARD = 2
    if time / FPS > 220:
        HARD = 3
    if time / FPS > 450:
        HARD = 4


def draw():
    Color = pygame.Color('black')
    font = pygame.font.Font(None, 50 * Size_k)
    text = font.render(f"{time // FPS} | {HARD}", True, Color)
    text_x = width - (width // 15 * Size_k) - text.get_width() // 2
    text_y = height // 20 * Size_k - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, Color, (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1 * Size_k)


def die():
    global pause
    pygame.mouse.set_visible(True)
    pause = False
    screen.fill((255, 255, 255))
    Color = pygame.Color('black')
    font = pygame.font.Font(None, 50 * Size_k)
    text = font.render(f"you dead!", True, Color)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, Color, (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1 * Size_k)


def game():
    global time
    if __name__ == '__main__':
        collor = pygame.Color('white')
        mouse_cursor = pygame.Surface((35 * 2, 35 * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(mouse_cursor, pygame.Color("black"),
                           (35, 35), 35, 3)

        difficulty()
        if HARD == 0:
            TIME_S = 0
        elif HARD == 1:
            TIME_S = 15
        elif HARD == 2:
            TIME_S = 10
        elif HARD == 3:
            TIME_S = 5
        elif HARD == 4:
            TIME_S = 2
        draw()

        time += 1
        if TIME_S == 0:
            pass
        elif TIME_S > 0:
            if (time / FPS) % TIME_S == 0:
                print('spawn')
                slow()
                Circal_dvd()
        x, y = pygame.mouse.get_pos()
        screen.blit(mouse_cursor, (x - 35, y - 35))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill(collor)



def play():
    global time, pause
    if __name__ == '__main__':
        collor = pygame.Color('white')
        screen.fill(collor)
        pygame.mouse.set_visible(False)
        running = True
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
            if pause:
                game()
        clock.tick(120)
    pygame.quit()


play()
