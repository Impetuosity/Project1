import pygame, sqlite3
from Button_class import Button
class Game:
    pass
def process():
    def update_raiting(data, time, points):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        sql_update_query = """INSERT INTO results (time, date, points) values(?, ?, ?)"""
        cur.executemany(sql_update_query, [(time, data, points)])
        con.commit()
        cur.close()
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    if True:
        update_raiting('23.04.23', '12:23', 123441)
    pygame.display.set_caption("Game")
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
