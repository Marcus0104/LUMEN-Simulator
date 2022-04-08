# C3G3 3.007 Virtual Prototype 

# relevant libs 
import pygame
import random
import math 
pygame.init()

# declaration 
screen = width,height = 800,600
fps = 60 
cellsize = 50 
padding = 70 # create identations from the window 
rows = cols = (width - 80) // cellsize 
print(rows, cols) 

pygame.init()
surface = pygame.display.set_mode(screen) 

# color options 
white = (255,255,255) 
black = (0,0,0) 
green = (0,255,0) 

# load img for chars 
char1 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char1.png")
char3 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\grab_driver.jpg")
char4 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char4.jpg")
char5 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char5.jpg")
char6 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char6.jpg")
char7 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char7.jpg")
char8 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\char8.jpg")

# calculate distance from mouse to prototype
def euclid_dist(mX, mY, x, y):
        dist = math.sqrt((mX - x)**2 + (mY - y)**2)

        if dist <= 60: 
            return True
        else: 
            return False 

running = True

# create an NPC object on the map 
class Cell_1: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char4
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))

    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 30 or self.x >= width - 30:
            self.x_speed *= -1 

        elif self.y <= 30 or self.y >= height - 30:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

class Cell_2: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char5
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))
    

    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 30 or self.x >= width - 30:
            self.x_speed *= -1 

        elif self.y <= 30 or self.y >= height - 30:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

class Cell_3: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char6
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))

    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 30 or self.x >= width - 30:
            self.x_speed *= -1 

        elif self.y <= 30 or self.y >= height - 30:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

class Cell_4: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char7
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))
    
    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 30 or self.x >= width - 30:
            self.x_speed *= -1 

        elif self.y <= 30 or self.y >= height - 30:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

class Cell_5: 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position
        self.x_speed = 2
        self.y_speed = 2 

        self.image = char8
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))
    
    def wander(self):
        self.x += self.x_speed 
        self.y += self.y_speed

        if self.x <= 30 or self.x >= width - 30:
            self.x_speed *= -1 

        elif self.y <= 30 or self.y >= height - 30:
            self.y_speed *= -1

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

class Grab_driver: 
    # make driving linear 
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = height - 20 #bottom of screen 
        self.y_speed = 12
        self.x_speed = 12

        self.image = char3
        self.image = pygame.transform.scale(self.image, (cellsize+20, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center = (self.x, self.y))

    def wander(self):
        if self.y <= 20: # height 
            self.y = height 
            self.x = random.randrange(20, width-20)

        else: 
            self.y -= self.y_speed

    def draw(self): 
        surface.blit(self.image, (self.x, self.y))

# include smoking zone 


cells_1 = []
for i in range(2): #instantiate N cells
    cell = Cell_1()
    cells_1.append(cell)

cells_2 = []
for i in range(2): #instantiate N cells
    cell = Cell_2()
    cells_2.append(cell)

cells_3 = []
for i in range(2): #instantiate N cells
    cell = Cell_3()
    cells_3.append(cell)

cells_4 = []
for i in range(1): #instantiate N cells
    cell = Cell_4()
    cells_4.append(cell)

cells_5 = []
for i in range(1): #instantiate N cells
    cell = Cell_5()
    cells_5.append(cell)


drivers = []
for i in range(1): 
    driver = Grab_driver()
    drivers.append(driver)

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
        
    for npc in cells_1: 
        npc.wander()
        npc.draw()

    for npc in cells_2: 
        npc.wander()
        npc.draw()

    for npc in cells_3: 
        npc.wander() 
        npc.draw() 

    for npc in cells_4:
        npc.wander() 
        npc.draw() 

    for npc in cells_5: 
        npc.wander()
        npc.draw() 
    
    (mX, mY) = pygame.mouse.get_pos()
    char1 = pygame.transform.scale(char1, (30, cellsize)) 
    surface.blit(char1, (mX, mY))

    for row in range(rows): 
        for col in range(cols): 
            for i in cells_1: # applies for drivers as well (not sure why) 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 


    for row in range(rows): 
        for col in range(cols): 
            for i in cells_2: # applies for drivers as well (not sure why) 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 
                    
    for row in range(rows): 
        for col in range(cols): 
            for i in cells_3: # applies for drivers as well (not sure why) 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 
                    
    for row in range(rows): 
        for col in range(cols): 
            for i in cells_4: # applies for drivers as well (not sure why) 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 

    for row in range(rows): 
        for col in range(cols): 
            for i in drivers: # applies for drivers as well (not sure why) 
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