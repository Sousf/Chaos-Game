import pygame
import random
import time
import random

import  os
pygame.init()
pygame.font.init() 


FPS = 200
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
dotSide = 2

# scaling_factor = 20
scr = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('fern')

# Colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# Data Structs
ALL_POINTS = [pygame.Rect(0, 0,dotSide,dotSide)]
RENDER_POINTS = [[pygame.Rect(0, 0,dotSide,dotSide)]]

NUM_POINTS = 3
# Initialise tracker point
# tracker_point = pygame.Rect(random.randint(5,SCREEN_WIDTH - 5), random.randint(5,SCREEN_WIDTH - 5),dotSide,dotSide)
# tracker_point.center = (tracker_point.x + (dotSide // 2), tracker_point.y + (dotSide // 2))
myfont = pygame.font.SysFont('Comic Sans MS', 30)




def main():
    clock = pygame.time.Clock()
    running = True
    begin = True
    iteration = 0
    scalex = random.randint(30,80)
    scaley = random.randint(30,80)
    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False


        scr.fill(CYAN)



        choice = randomise()
        # print(choice)

        newx, newy = get_new_point(choice, [ALL_POINTS[-1][0], ALL_POINTS[-1][1]])
        # print("old : ", [ALL_POINTS[-1].x, ALL_POINTS[-1].y], "new : ", newx, newy)
        # print(ALL_POINTS[-1].x, ALL_POINTS[-1].y)
        ALL_POINTS.append((newx, newy))

        for point in ALL_POINTS:
            # old range for x: (-2.1820, 2.6558)
            # old range for y: (0, 9.9983)
            # testx = (((point[0] + 2.1820) * (800)) / (2.6558 + 2.1820)) + 0
            # testy = (((point[1] + 0) * (800)) / (9.9983)) + 0
            # pygame.draw.rect(scr,GREEN, (testx,testy,dotSide,dotSide))
            pygame.draw.rect(scr,BLACK, (point[0]*scalex + 500,-point[1]*scaley + 600,dotSide,dotSide))
            # pygame.draw.rect(scr,BLACK,pygame.Rect(500, 500,20,20))

        textsurface = myfont.render(f'Iteration: {iteration}', False, (0, 0, 0))
        scr.blit(textsurface,(0,0))
        iteration += 1
        # if iteration == 10:
        #     print(ALL_POINTS)
        #     break
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()



    
def randomise():
    my_list = [1] * 1 + [2] * 85 + [3] * 7 + [4] * 7
    return random.choice(my_list)


def get_new_point(choice, coords):
    if choice == 1:
        newx = 0
        newy = 0.16*coords[1]
    elif choice == 2:
        newx = 0.85*coords[0] + 0.04*coords[1]
        newy = -0.04*coords[0] + 0.85*coords[1] + 1.6
    elif choice == 3:
        newx = 0.2*coords[0] - 0.26*coords[1]
        newy = 0.23*coords[0] + 0.22*coords[1] + 1.6
    else:
        newx = -0.15*coords[0] + 0.28*coords[1]
        newy = 0.26*coords[0] + 0.24*coords[1] + 0.44

    return newx, newy




if __name__ == "__main__":
    main()
