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
buttonlist = []
pos = []
validmoves = []
clicked = False
bbut = pygame.transform.scale(pygame.image.load("bb.png"), (60, 60))
wbut = pygame.transform.scale(pygame.image.load("wb.png"), (60, 60))


def get_screen_loc(x, y):
    offset = 90
    tilesize = 80
    gridsize = 8
    newx = round((tilesize * x) + offset)
    newy = round((tilesize * y) + offset)
    return newx, newy


class Nupp:
    color = ""
    loc = []
    list_loc = 0
    selected = False

    def __init__(self, color, locx, locy, list_loc):
        self.loc = [locx, locy]
        self.color = str(color)
        self.list_loc = list_loc

    def move(self, locx, locy):
        self.loc = [locx, locy]

    def draw(self):
        if self.color == "black":
            screen.blit(bbut, (get_screen_loc(self.loc[0], self.loc[1])[0], get_screen_loc(self.loc[0], self.loc[1])[1]))
        elif self.color == "white":
            screen.blit(wbut, (get_screen_loc(self.loc[0], self.loc[1])[0], get_screen_loc(self.loc[0], self.loc[1])[1]))

    def clicked(self):
        self.selected = True
        for niba in buttonlist:
            if niba.selected and not niba.list_loc == self.list_loc:
                niba.selected = False
        # check validtiles for not containing anything
        for currenttile in validtiles:
            foundbutton = False
            for currentbutton in buttonlist:
                print(currenttile, currentbutton.loc)
                if (currentbutton.loc == currenttile) or foundbutton:
                    foundbutton = True
                    pass
                else:
                    validmoves.append(currenttile)
        print(validmoves)

    def destroy(self):
        buttonlist[self.list_loc - 1] = "nun"


n = 0
for yy in range(3):
    for xx in range(8):
        currentloc = (xx, yy)
        if currentloc in validtiles:
            n += 1
            bb = Nupp("black", xx, yy, n)
            buttonlist.append(bb)
        else:
            pass

for yy in range(5, 8):
    for xx in range(8):
        currentloc = (xx, yy)
        if currentloc in validtiles:
            n += 1
            wb = Nupp("white", xx, yy, n)
            buttonlist.append(wb)
        else:
            pass

while True:
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
        for button in buttonlist:
            if button == "nun":
                pass
            else:
                test_rect = pygame.Rect(get_screen_loc(button.loc[0], button.loc[1]), (60, 60))
                if test_rect.collidepoint(pos[0], pos[1]):
                    button.clicked()

    # draw all the shit
    screen.blit(pygame.transform.scale(pygame.image.load("kabelaud.png"), window_size), (0, 0))
    for button in buttonlist:
        if button == "nun":
            pass
        else:
            if button.selected:
                pygame.draw.circle(screen, pygame.Color("Green"), get_screen_loc(button.loc[0] + 0.4, button.loc[1] + 0.4), 40)
            button.draw()
    for move in validmoves:
        pygame.draw.circle(screen, pygame.Color("Blue"), get_screen_loc(move[0] + 0.4, move[1] + 0.4), 20)
    pygame.display.flip()
    clock.tick(30)
