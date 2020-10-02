import pygame
pygame.init()
HEIGHT = 5
WIDTH = HEIGHT
SCALE = 100


RED = (255, 0, 0)
ORANGE = (255, 200, 0)
BLACK = (0, 0, 0)

MATRIX = [[-1 for i in range(5)] for j in range(5)]
print(MATRIX)

screen = pygame.display.set_mode((HEIGHT*SCALE, WIDTH*SCALE))
pygame.display.set_caption("Game")
background_colour = (255, 255, 255)
screen.fill(background_colour)

def setCIRCLE(x, y):
    x_ = int(x/SCALE)*SCALE+int(SCALE/2)
    y_ = int(y/SCALE)*SCALE+int(SCALE/2)
    pygame.draw.circle(screen, RED, (x_, y_), int(SCALE/2.5), int(SCALE/20))

def setCROSS(x, y):
    x_ = int(x/SCALE)*SCALE+int(SCALE/2)
    y_ = int(y/SCALE)*SCALE+int(SCALE/2)
    pygame.draw.line(screen, ORANGE, [x_-int(SCALE/3), y_+int(SCALE/3)], [x_+int(SCALE/3), y_-int(SCALE/3)], int(SCALE/20))
    pygame.draw.line(screen, ORANGE, [x_ - int(SCALE / 3), y_ - int(SCALE / 3)], [x_ + int(SCALE / 3), y_ + int(SCALE / 3)],int(SCALE/20))

def isWin():
    for i in range(HEIGHT):
        if MATRIX[i][0] != -1:
            k = MATRIX[i][0]
        else:
            continue
        S = True
        for j in range(WIDTH):
            if k != MATRIX[i][j]:
                S = False
                break
        if S:
            return ([i*SCALE+int(SCALE/2), int(SCALE/5)], [i*SCALE+int(SCALE/2), WIDTH*SCALE - int(SCALE/5)])
    for j in range(WIDTH):
        if MATRIX[0][j] != -1:
            k = MATRIX[0][j]
        else:
            continue
        S = True
        for i in range(HEIGHT):
            if k != MATRIX[i][j]:
                S = False
                break
        if S:
            return ([int(SCALE/5), j*SCALE+int(SCALE/2)], [HEIGHT*SCALE - int(SCALE/5), j*SCALE+int(SCALE/2)])
    k = MATRIX[0][0]
    S = True
    for i in range(WIDTH):
        if k != MATRIX[i][i] or MATRIX[i][i] == -1:
            S = False
            break
    if S:
        return ([int(SCALE/5), int(SCALE/5)], [WIDTH*SCALE - int(SCALE/5), HEIGHT*SCALE - int(SCALE/5)])

    k = MATRIX[HEIGHT-1][0]
    S = True
    for i in range(WIDTH):
        if k != MATRIX[i][HEIGHT-i-1] or MATRIX[HEIGHT-i-1][i] == -1:
            S = False
            break
    if S:
        return ([int(SCALE/5), HEIGHT*SCALE - int(SCALE/5)], [WIDTH*SCALE - int(SCALE/5), int(SCALE/5)])
    return False

for i in range(0, HEIGHT):
    pygame.draw.line(screen, BLACK, [i * SCALE, 0], [i * SCALE, WIDTH * SCALE])
for i in range(0, WIDTH):
    pygame.draw.line(screen, BLACK, [0, i * SCALE], [HEIGHT * SCALE, i * SCALE])
pygame.display.flip()

running = True
STEP = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(STEP)
            if STEP % 2 == 1:
                x, y = event.pos
                if MATRIX[int(x/SCALE)][int(y/SCALE)] == -1:
                    setCIRCLE(x, y)
                    STEP += 1
                    pygame.display.flip()
                    MATRIX[int(x / SCALE)][int(y / SCALE)] = 0
            elif event.button == 1 and STEP % 2 == 0:
                x, y = event.pos
                if MATRIX[int(x / SCALE)][int(y / SCALE)] == -1:
                    setCROSS(x, y)
                    STEP += 1
                    pygame.display.flip()
                    MATRIX[int(x / SCALE)][int(y / SCALE)] = 1
        if isWin():
            p1, p2 = isWin()
            pygame.draw.line(screen, BLACK, p1, p2, int(SCALE/20))
            pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False