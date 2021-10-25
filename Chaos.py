import pygame
import random
import time
pygame.init()
pygame.font.init() 


FPS = 200
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
dotSide = 1

# scaling_factor = 20
scr = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Random Dot')

# Colours
RED = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


# Data Structs
INIT_POINTS = []
ALL_POINTS = []
NUM_POINTS = 3
# Initialise tracker point
tracker_point = pygame.Rect(random.randint(5,SCREEN_WIDTH - 5), random.randint(5,SCREEN_WIDTH - 5),dotSide,dotSide)
tracker_point.center = (tracker_point.x + (dotSide // 2), tracker_point.y + (dotSide // 2))
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    running = True
    begin = True
    iteration = 0
    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False


        scr.fill(RED)


        # Initialise
        if begin == True:
            InitialisePoints()
            curr_point = tracker_point
            begin = False


        for p in INIT_POINTS:
            pygame.draw.rect(scr,BLACK,p)
        pygame.draw.rect(scr,WHITE,tracker_point)


        # Start the simulation
        curr_point = roll_and_draw(curr_point)
        for point in ALL_POINTS:
            pygame.draw.rect(scr,BLACK,point)


        textsurface = myfont.render(f'Initial points :{NUM_POINTS}, Iteration: {iteration}', False, (0, 0, 0))
        scr.blit(textsurface,(0,0))
        iteration += 1
        pygame.display.update()
    pygame.quit()




def InitialisePoints():
    for i in range(NUM_POINTS):
        rect = pygame.Rect(random.randint(5,SCREEN_WIDTH - 5), random.randint(5,SCREEN_WIDTH - 5),dotSide,dotSide)
        rect.center = (rect.x + (dotSide // 2), rect.y + (dotSide // 2))
        INIT_POINTS.append(rect)


def InitialiseSquarePoints():
    pass



def roll_and_draw(curr_point):
    # roll a number
    num_rand = random.randint(0,NUM_POINTS-1)
    
    t_x, t_y = INIT_POINTS[num_rand].center
    v = pygame.Vector2()
    v.xy = t_x - curr_point.centerx, t_y - curr_point.centery
    new_vec = v*0.5
    new_point = curr_point.move(new_vec)

    # print(new_vec)

    ALL_POINTS.append(new_point)
    return new_point

    





if __name__ == "__main__":
    main()
