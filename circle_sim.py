import math
import pygame
import random
import time
pygame.init()
pygame.font.init() 
pi = math.pi

myfont = pygame.font.SysFont('Comic Sans MS', 30)
def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

def get_points():
    return [pygame.Rect(p[0]+(SCREEN_WIDTH // 2), p[1]+(SCREEN_HEIGHT // 2),SIDE,SIDE) for p in ALL_POINTS]

FPS = 50
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
dotSide = 1
RADIUS = 400
SIDE = 1
N = 400

# Colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# scaling_factor = 20
scr = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Circle Sim')


# Data Structs
ALL_POINTS = PointsInCircum(RADIUS, N)
Points = get_points()





def draw_line(MULTIPLIER):
    lines = []
    for i,rect in enumerate(Points):
        target_index = MULTIPLIER*i
        if target_index > len(Points)-1:
            target_index = target_index % len(Points)
        t_pointx, t_pointy = Points[target_index].x, Points[target_index].y
        lines.append([rect.x,rect.y, t_pointx, t_pointy])
    return lines

def main():
    MULTIPLIER = 1
    clock = pygame.time.Clock()
    running = True
    begin = True

    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False


        scr.fill(WHITE)
        lines = draw_line(MULTIPLIER)
        for i, rect in enumerate(Points):
            pygame.draw.rect(scr,BLACK,rect)

        for i in range(0, len(lines)-1):
            pygame.draw.line(scr, BLACK, [lines[i][0], lines[i][1]], [lines[i][2], lines[i][3]], 2)
        # print(len(lines[0][0]))


            # firstx, firsty = Points[0].x, Points[0].y
            # lastx, lasty = Points[-2].x, Points[-2].y
            # pygame.draw.line(scr, BLACK, [firstx, firsty], [lastx, lasty], 2)

        textsurface = myfont.render(f'Multiplier: {MULTIPLIER}', False, (0, 0, 0))
        scr.blit(textsurface,(0,0))
        clock.tick(2)
        MULTIPLIER = MULTIPLIER +1
        pygame.display.update()
    pygame.quit()




if __name__ == "__main__":
    main()
    # print(ALL_POINTS)

# print(PointsInCircum(20,100))