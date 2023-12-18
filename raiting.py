import pygame, sqlite3
from Button_class import Button
class Raiting:
    pass
def raiting():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Raiting")
    name = pygame.font.SysFont(None, 200).render('Results', False,
                                             (255, 255, 255))
    screen.blit(name, (700, 76))
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
        screen.blit(point, (500, 300 + i * 75))
        date = pygame.font.SysFont(None, 100).render(str(spisok[points[i]][0]), False,
                                             (255, 255, 255))
        screen.blit(date, (800, 300 + i * 75))
        time = pygame.font.SysFont(None, 100).render(str(spisok[points[i]][1]), False,
                                             (255, 255, 255))
        screen.blit(time, (1200, 300 + i * 75))
    button = Button(1700, 960, 200, 100, (255, 255, 255), 'Exit', 5, 20, 128)
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.is_clicked(mouse_pos):
                    pass
    button.draw(screen)
    con.commit()
    cur.close()
    pygame.display.flip()
    pygame.quit()