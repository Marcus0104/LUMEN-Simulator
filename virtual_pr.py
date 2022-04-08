# relevant libs 
import pygame
import random
import math 
pygame.init()

# declaration 
screen = width,height = 800,600
fps = 60 
cellsize = 50 
padding = 70 # create space around an element 
rows = cols = (width - 80) // cellsize 
print(rows, cols) 

pygame.init()
surface = pygame.display.set_mode(screen) 

# color options 
white = (255,255,255) 
black = (0,0,0) 
green = (0,255,0) 

char1 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char1.png")
char2 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char2.png")
char3 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\grab_driver.jpg")


# update based on your directory thanks! 
char1 = pygame.transform.scale(char1, (30, cellsize)) 
# char2 = pygame.transform.scale(char2, (30, cellsize)) 

# calculate distance from mouse to prototype
def euclid_dist(mX, mY, x, y):
        dist = math.sqrt((mX - x)**2 + (mY - y)**2)

        if dist <= 60: 
            return True
        else: 
            return False 

running = True

# create an NPC object on the map 
class Cell: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char2
        self.image = pygame.transform.scale(self.image, (40, cellsize))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))
    

    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 20 or self.x >= width - 20:
            self.x_speed *= -1 

        elif self.y <= 20 or self.y >= height - 20:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))
    
class Grab_driver: 
    # make driving linear 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 6
        self.y_speed = 6

        self.image = char3
        self.image = pygame.transform.scale(self.image, (cellsize+20, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center = (self.x, self.y))

    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 20 or self.x >= width - 20:
            self.x_speed *= -1 

        elif self.y <= 20 or self.y >= height - 20:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

        

cells = []
for i in range(5): #instantiate N cells
    cell = Cell()
    cells.append(cell)

drivers = []
for i in range(2): 
    driver = Grab_driver()
    cells.append(driver)

while running:
    warm_col = (255, random.randint(0, 255), 0)
    surface.fill(black)
    collision_tol = 10 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            # upon closing the window with mouse 
            running = False 

    for driver in drivers:
        driver.wander() 
        driver.draw()
        
    for npc in cells: 
        npc.wander()
        npc.draw()

    (mX, mY) = pygame.mouse.get_pos()
    surface.blit(char1, (mX, mY))

    for row in range(rows): 
        for col in range(cols): 
            for i in cells: # applies for drivers as well (not sure why) 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 
                    
                   
                    

    pygame.display.update() 
    pygame.time.Clock().tick(fps) 
    pygame.mouse.set_visible(False) 

pygame.quit() 
