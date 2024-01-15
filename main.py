import datetime
import math
import pygame
import random
import sqlite3
import time as tr
import sys
import subprocess

# Инициализация
pygame.init()
pygame.mixer.music.load('geoffplaysguitar - The Only Thing I Know For Real (Instrumental) -Geoffrey Day, Andrew Baena,'
                        ' The Maniac Agenda).wav')

pygame.mixer.music.set_volume(0.5)
s_d = pygame.mixer.Sound('die_s.mp3')
s_s = pygame.mixer.Sound('spawn_s.mp3')
infoObject = pygame.display.Info()
print(infoObject.current_w, infoObject.current_h)
width, height = (infoObject.current_w, infoObject.current_h)
time = 0
pause = True
Size_k = width / 1920
RADIUS = int(35 * Size_k)
FPS = 120
HARD = 0
pygame.init()
# Установка размеров окна
screen = pygame.display.set_mode((width, height))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, x_s, y_s):
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
        self.rect.x = x_coord
        self.rect.y = y_coord
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
        self.y_s = int(y_s * Size_k)
        self.x_s = int(x_s * Size_k)

    def update(self):
        if self.lifetime < 0:
            self.kill()
        self.rect = self.rect.move(self.x_s, self.y_s)
        self.lifetime -= 1


class Enemies_slowly(pygame.sprite.Sprite):
    def __init__(self, x_coord, y_coord, x_s, y_s):
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
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.y_s = int(y_s * Size_k)
        self.x_s = int(x_s * Size_k)

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
    def __init__(self, x_coord, y_coord, x_s, y_s):
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
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.y_s = int(y_s * Size_k)
        self.x_s = int(x_s * Size_k)

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
        self.player_speed = int(9 * Size_k)

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
    for _ in range(NUM):
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
    font = pygame.font.Font(None, int(50 * Size_k))
    text = font.render(f"{time // FPS} | {HARD}", True, Color)
    text_x = width - (int(width // 15 * Size_k)) - text.get_width() // 2
    text_y = int(height // 20 * Size_k) - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, Color, (text_x - 10, text_y - 10,
                                     text_w + 20, text_h + 20), int(1 * Size_k))


def die():
    global pause, ps, time, FPS
    pygame.mouse.set_visible(True)
    s_d.play()
    pygame.mixer.music.stop()
    pause = False
    screen.fill((255, 255, 255))
    Color = pygame.Color('black')
    font = pygame.font.Font(None, int(50 * Size_k))
    text = font.render(f"you are dead!", True, Color)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, Color, (text_x - 10, text_y - 10,
                                     text_w + 20, text_h + 20), 1)
    ps = time // FPS
    con = sqlite3.connect('films_db.sqlite')
    d = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M").split('-')
    cr = con.cursor()
    cr.execute("""INSERT INTO results VALUES(?, ?, ?)""", (d[-1], d[0], ps))
    con.commit()
    con.close()
    pygame.display.update()
    tr.sleep(3)
    python = sys.executable
    subprocess.call([python, __file__])
    sys.exit()


def game(s):
    global time
    if __name__ == '__main__':
        collor = pygame.Color('white')
        mouse_cursor = pygame.Surface((RADIUS * 2, RADIUS * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(mouse_cursor, pygame.Color("black"),
                           (RADIUS, RADIUS), RADIUS, int(3 * Size_k))

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
                s_s.play()
                slow()
                Circal_dvd()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        s.blit(mouse_cursor, (mouse_x - RADIUS, mouse_y - RADIUS))
        all_sprites.update()
        all_sprites.draw(s)
        pygame.display.flip()
        s.fill(collor)

class Batton:
    def __init__(self, text, step):
        self.Color = pygame.Color('white')
        font = pygame.font.Font(None, int(150 * Size_k))
        self.text = font.render(text, True, self.Color)
        self.text_x = width - (int(width // 2)) - self.text.get_width() // 2
        self.text_y = int(height * step * Size_k) - self.text.get_height() // 2
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()

    def draw_but(self):
        screen.blit(self.text, (self.text_x, self.text_y))
        pygame.draw.rect(screen, self.Color, (width * 0.5 - width * 0.1 - int(20 * Size_k), self.text_y - int(20 * Size_k),
                                         width * 0.2 + int(40 * Size_k), self.text_h + int(40 * Size_k)), int(2 * Size_k))

    def push(self):
        x, y = pygame.mouse.get_pos()
        if self.text_x <= x <= (self.text_x + self.text_w) and self.text_y <= y <= (self.text_y + self.text_h):
            return True
        else:
            return False


B_S = Batton('Start', 0.3)
B_R = Batton('Result', 0.45)
B_Q = Batton('Quite', 0.6)

def play(s):
    global time, pause
    if __name__ == '__main__':
        pygame.mixer.music.play()
        collor = pygame.Color('white')
        s.fill(collor)
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
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            pygame.mixer.music.pause()
                        else:
                            pause = True
                            pygame.mouse.set_pos(mouse_x, mouse_y)
                            pygame.mixer.music.unpause()
            if pause:
                game(s)
        clock.tick(120)
    pygame.quit()


# Инициализация
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
# Установка размеров окна
win = pygame.display.set_mode((width, height))

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Шрифты
font = pygame.font.SysFont(None, 128)

# Тексты
back_text = font.render('Back', True, white)
end_btn_text = font.render('Return to lobby', True, white)

# Основной цикл
run = True
while run:
    win.fill(black)

    # Рисуем кнопки

    # Рисуем тексты на кнопках
    B_S.draw_but()
    B_R.draw_but()
    B_Q.draw_but()
    name = pygame.font.SysFont(None, int(200 * Size_k)).render('Just Survive', False,
                                                 (255, 255, 255))
    win.blit(name, (int(555 * Size_k), int(76 * Size_k)))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if B_S.push():
                # Открываем обычное окно
                print(width, height)
                simple_win = pygame.display.set_mode((width, height))
                simple_win.fill(black)
                ps = 0
                play(simple_win)
                run = False

            elif B_R.push():
                # Открываем окно с кнопкой для возврата
                sub_win = pygame.display.set_mode((width, height))
                sub_win.fill(black)
                pygame.draw.rect(sub_win, (255, 255, 255), (int(width * 0.78), int(height * 0.88), int(width * 0.21), int(height * 0.09)),
                                 int(5 * Size_k), int(20 * Size_k))
                sub_win.blit(back_text, (int(1600 * Size_k), int(964 * Size_k)))

                name = pygame.font.SysFont(None, int(200 * Size_k)).render('Results', False,
                                                             (255, 255, 255))
                sub_win.blit(name, (int(700 * Size_k), int(76 * Size_k)))
                con = sqlite3.connect('films_db.sqlite')
                cur = con.cursor()
                results = cur.execute("""SELECT * FROM results""").fetchall()
                con.close()
                points = []
                spisok = {}
                for elem in results:
                    points.append(elem[-1])
                    spisok[elem[-1]] = [elem[1], elem[0]]
                points = sorted(points, reverse=True)
                for i in range(len(points)):
                    if i == 7:
                        break
                    point = pygame.font.SysFont(None, int(100 * Size_k)).render(str(points[i]), False,
                                                                  (255, 255, 255))
                    sub_win.blit(point, (int(500 * Size_k), int((300 + i * 75) * Size_k)))
                    date = pygame.font.SysFont(None, int(100 * Size_k)).render(str(spisok[points[i]][0]), False,
                                                                 (255, 255, 255))
                    sub_win.blit(date, (int(800 * Size_k), int((300 + i * 75) * Size_k)))
                    time_surf = pygame.font.SysFont(None, int(100 * Size_k)).render(str(spisok[points[i]][1]), False,
                                                                 (255, 255, 255))
                    sub_win.blit(time_surf, (int(1200 * Size_k), int((300 + i * 75) * Size_k)))
                pygame.display.update()
                sub_run = True
                while sub_run:
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.QUIT:
                            run = False
                            sub_run = False
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            sub_x, sub_y = pygame.mouse.get_pos()
                            if int(1500 * Size_k) <= sub_x <= int(1912 * Size_k) and int(960 * Size_k) <= sub_y\
                                    <= int(1060 * Size_k):
                                sub_run = False

            elif B_Q.push():
                # Завершаем игру
                run = False

    pygame.display.update()

# Завершение
pygame.quit()
