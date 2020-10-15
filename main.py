import pygame
pygame.init()
HEIGHT = 20
WIDTH = HEIGHT
SCALE = 30


RED = (255, 0, 0)
ORANGE = (255, 200, 0)
BLACK = (0, 0, 0)

MATRIX = [[-1 for i in range(WIDTH)] for j in range(HEIGHT)]
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

# def isWin():
#     for i in range(HEIGHT):
#         if MATRIX[i][0] != -1:
#             k = MATRIX[i][0]
#         else:
#             continue
#         S = True
#         for j in range(WIDTH):
#             if k != MATRIX[i][j]:
#                 S = False
#                 break
#         if S:
#             return ([i*SCALE+int(SCALE/2), int(SCALE/5)], [i*SCALE+int(SCALE/2), WIDTH*SCALE - int(SCALE/5)])
#     for j in range(WIDTH):
#         if MATRIX[0][j] != -1:
#             k = MATRIX[0][j]
#         else:
#             continue
#         S = True
#         for i in range(HEIGHT):
#             if k != MATRIX[i][j]:
#                 S = False
#                 break
#         if S:
#             return ([int(SCALE/5), j*SCALE+int(SCALE/2)], [HEIGHT*SCALE - int(SCALE/5), j*SCALE+int(SCALE/2)])
#     k = MATRIX[0][0]
#     S = True
#     for i in range(WIDTH):
#         if k != MATRIX[i][i] or MATRIX[i][i] == -1:
#             S = False
#             break
#     if S:
#         return ([int(SCALE/5), int(SCALE/5)], [WIDTH*SCALE - int(SCALE/5), HEIGHT*SCALE - int(SCALE/5)])
#
#     k = MATRIX[HEIGHT-1][0]
#     S = True
#     for i in range(WIDTH):
#         if k != MATRIX[i][HEIGHT-i-1] or MATRIX[HEIGHT-i-1][i] == -1:
#             S = False
#             break
#     if S:
#         return ([int(SCALE/5), HEIGHT*SCALE - int(SCALE/5)], [WIDTH*SCALE - int(SCALE/5), int(SCALE/5)])
#     return False
def isWin():
    for i in range(HEIGHT):
        countx = 0
        counto = 0
        for j in range(WIDTH):
            if(MATRIX[i][j] == 1):
                countx += 1
                counto = 0
            if (MATRIX[i][j] == 0):
                counto += 1
                countx = 0
            if(MATRIX[i][j] == -1):
                countx = 0
                counto = 0
            if(countx == 5 or counto == 5):
                return ([i * SCALE + int(SCALE / 2), (j+1)*SCALE - int(SCALE/5)],
                        [i * SCALE + int(SCALE / 2), (j-4) * SCALE + int(SCALE / 5)])
    for j in range(WIDTH):
        countx = 0
        counto = 0
        for i in range(HEIGHT):
            if(MATRIX[i][j] == 1):
                countx += 1
                counto = 0
            if (MATRIX[i][j] == 0):
                counto += 1
                countx = 0
            if(MATRIX[i][j] == -1):
                countx = 0
                counto = 0
            if(countx == 5 or counto == 5):
                 return ([(i+1) * SCALE - int(SCALE/5), j*SCALE+int(SCALE/2)],
                         [(i-4) * SCALE + int(SCALE/5), j*SCALE+int(SCALE/2)])

    for k in range(HEIGHT):
        for g in range(WIDTH):
            countx = 0
            counto = 0
            for i in range(5):
                if (i+k >= HEIGHT or i+g >= WIDTH):
                    continue
                if (MATRIX[i+k][i+g] == 1):
                    countx += 1
                    counto = 0
                if (MATRIX[i+k][i+g] == 0):
                    counto += 1
                    countx = 0
                if (MATRIX[i+k][i+g] == -1):
                    countx = 0
                    counto = 0
                if (countx == 5 or counto == 5):
                    return ([k * SCALE + int(SCALE / 5),g * SCALE + int(SCALE / 5)],
                            [(k+5) * SCALE - int(SCALE / 5), (g+5) * SCALE - int(SCALE / 5)])
    for k in range(HEIGHT):
        for g in range(WIDTH):
            countx = 0
            counto = 0
            for i in range(5):
                if (i+k >= HEIGHT or g-i < 0):
                    continue
                if (MATRIX[i+k][g-i] == 1):
                    countx += 1
                    counto = 0
                if (MATRIX[i+k][g-i] == 0):
                    counto += 1
                    countx = 0
                if (MATRIX[i+k][g-i] == -1):
                    countx = 0
                    counto = 0
                if (countx == 5 or counto == 5):
                    return ([k * SCALE + int(SCALE / 5),(g+1) * SCALE - int(SCALE / 5)],
                            [(k+5) * SCALE - int(SCALE / 5), (g-4) * SCALE + int(SCALE / 5)])
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
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
        if event.type == pygame.QUIT:
            running = False