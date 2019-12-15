import pygame, sys

pygame.init()
window_size = window_width, window_height = 800, 800
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
validtiles = [(1, 0), (3, 0), (5, 0), (7, 0),
              (0, 1), (2, 1), (4, 1), (6, 1),
              (1, 2), (3, 2), (5, 2), (7, 2),
              (0, 3), (2, 3), (4, 3), (6, 3),
              (1, 4), (3, 4), (5, 4), (7, 4),
              (0, 5), (2, 5), (4, 5), (6, 5),
              (1, 6), (3, 6), (5, 6), (7, 6),
              (0, 7), (2, 7), (4, 7), (6, 7)]
blacklist = []
whitelist = []
pos = []
clicked = False
bbut = pygame.transform.scale(pygame.image.load("bb.png"), (60, 60))
wbut = pygame.transform.scale(pygame.image.load("wb.png"), (60, 60))


def get_screen_loc(x, y):
    offset = 90
    tilesize = 80
    gridsize = 8
    newx = (tilesize * x) + offset
    newy = (tilesize * y) + offset
    return newx, newy


class Nupp:
    color = ""
    loc = []

    def __init__(self, color, locx, locy):
        self.loc = [locx, locy]
        self.color = str(color)

    def move(self, locx, locy):
        self.loc = [locx, locy]

    def draw(self):
        if self.color == "black":
            screen.blit(bbut, (get_screen_loc(nupp.loc[0], nupp.loc[1])[0], get_screen_loc(nupp.loc[0], nupp.loc[1])[1]))
        elif self.color == "white":
            screen.blit(wbut,
                        (get_screen_loc(nupp.loc[0], nupp.loc[1])[0], get_screen_loc(nupp.loc[0], nupp.loc[1])[1]))



for yy in range(3):
    for xx in range(8):
        currentloc = (xx, yy)
        if currentloc in validtiles:
            bb = Nupp("black", xx, yy)
            blacklist.append(bb)
        else:
            pass

for yy in range(5, 8):
    for xx in range(8):
        currentloc = (xx, yy)
        if currentloc in validtiles:
            wb = Nupp("white", xx, yy)
            whitelist.append(wb)
        else:
            pass

while True:
    print("___")
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked = True

    if clicked:
        clicked = False



    # draw all the shit
    screen.blit(pygame.transform.scale(pygame.image.load("kabelaud.png"), window_size), (0, 0))
    for n in Nupp:
        


    pygame.display.flip()
    clock.tick(30)
