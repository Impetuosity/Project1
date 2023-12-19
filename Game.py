import pygame, sqlite3, math


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(enemies)
        self.x2 = x2 # это фича
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
        self.player_speed = 15

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

# Инициализация
pygame.init()

# Установка размеров окна
win = pygame.display.set_mode((1920, 1080))

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Шрифты
font = pygame.font.SysFont(None, 128)

# Тексты
text1 = font.render('Start', True, white)
text2 = font.render('Result', True, white)
text3 = font.render('Quit', True, white)
back_text = font.render('Back', True, white)
end_btn_text = font.render('Return to lobby', True, white)

# Основной цикл
run = True
while run:
    win.fill(black)
    
    # Рисуем кнопки
    pygame.draw.rect(win, (255, 255, 255), (751, 409 + 0 * 150, 422, 100), 5, 20)
    pygame.draw.rect(win, (255, 255, 255), (751, 409 + 1 * 150, 422, 100), 5, 20)
    pygame.draw.rect(win, (255, 255, 255), (751, 409 + 2 * 150, 422, 100), 5, 20)
    
    # Рисуем тексты на кнопках
    win.blit(text1, (851, 414))
    win.blit(text2, (811, 564))
    win.blit(text3, (851, 714))
    name = pygame.font.SysFont(None, 200).render('Just Survive', False,
                                             (255, 255, 255))
    win.blit(name, (555, 76))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 751 <= x <= 1173 and 409 <= y <= 509:
                # Открываем обычное окно
                simple_win = pygame.display.set_mode((1920, 1080))
                simple_win.fill(black)
    
                enemies = pygame.sprite.Group()
                all_sprites = pygame.sprite.Group()
                enemies = pygame.sprite.Group()
                Border(0, 0, 1920, 0)
                Border(0, 1920, 1080, 1920)
                Border(0, 0, 0, 1080)
                Border(1920, 0, 1920, 1080)
                player = Player()
                all_sprites.add(player)
                play()
                

            elif 751 <= x <= 1173 and 559 <= y <= 659:
                # Открываем окно с кнопкой для возврата
                sub_win = pygame.display.set_mode((1920, 1080))
                sub_win.fill(black)
                pygame.draw.rect(sub_win, (255, 255, 255), (1500, 960, 412, 100), 5, 20)
                sub_win.blit(back_text, (1600, 964))
                
                name = pygame.font.SysFont(None, 200).render('Results', False,
                                             (255, 255, 255))
                sub_win.blit(name, (700, 76))
                con = sqlite3.connect('films_db.sqlite')
                cur = con.cursor()
                results = cur.execute("""SELECT * FROM results""").fetchall()
                points = []
                spisok = {}
                for elem in results:
                    points.append(elem[-1])
                    spisok[elem[-1]] = [elem[1], elem[0]]
                points = sorted(points, reverse=True)
                for i in range(len(points)):
                    if i == 9:
                        break
                    point = pygame.font.SysFont(None, 100).render(str(points[i]), False,
                                             (255, 255, 255))
                    sub_win.blit(point, (500, 300 + i * 75))
                    date = pygame.font.SysFont(None, 100).render(str(spisok[points[i]][0]), False,
                                             (255, 255, 255))
                    sub_win.blit(date, (800, 300 + i * 75))
                    time = pygame.font.SysFont(None, 100).render(str(spisok[points[i]][1]), False,
                                             (255, 255, 255))
                    sub_win.blit(time, (1200, 300 + i * 75))
                pygame.display.update()
                sub_run = True
                while sub_run:
                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.QUIT:
                            run = False
                            sub_run = False
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            sub_x, sub_y = pygame.mouse.get_pos()
                            if 1500 <= sub_x <= 1912 and 960 <= sub_y <= 1060:
                                sub_run = False

            elif 751 <= x <= 1173 and 709 <= y <= 809:
                # Завершаем игру
                run = False

    pygame.display.update()

# Завершение
pygame.quit()
