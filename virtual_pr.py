# relevant libs 
import pygame
import random
import math
pygame.init()

# declaration 
screen = width,height = 800,600
fps = 60 
cellsize = 50 
padding = 40 # create identations from the window 
rows = cols = (width - 50) // cellsize 
print(rows, cols) 

pygame.init()
surface = pygame.display.set_mode(screen) 
pygame.display.set_caption('LUMEN Simulator')

# color options 
white = (255,255,255) 
black = (0,0,0) 
bright_red = (238, 75, 43)

# load img for chars 
char1 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char1.png")
char3 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\grab_driver.jpg")
char4 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char4.jpg")
char5 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char5.jpg")
char6 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char6.jpg")
char7 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char7.jpg")
char8 = pygame.image.load(r"C:\Users\marcu\Desktop\3.007\virtual_proto\Images\char8.jpg")

# calculate distance from mouse to prototype
def euclid_dist(mX, mY, x, y):
        dist = math.sqrt((mX - x)**2 + (mY - y)**2)

        if dist <= 60: 
            return True
        else: 
            return False 

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

class Cell_3: # SMOKER
    def __init__(self):
        self.x = random.randrange(20, width-20) #x position
        self.y = random.randrange(20, height-20) #y position

        self.image = char6
        self.image = pygame.transform.scale(self.image, (cellsize, cellsize+20))
        self.rect = pygame.Surface.get_rect(self.image, center= (self.x, self.y))

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

# list to store all rect objects 
# except smoker and grab driver 
rects = [] 
cells_1 = []
for i in range(2): #instantiate N cells
    cell = Cell_1()
    cells_1.append(cell)
    rects.append(cell) 

cells_2 = []
for i in range(2): #instantiate N cells
    cell = Cell_2()
    cells_2.append(cell)
    rects.append(cell)

cells_3 = [] # SMOKERS, exclude from rects
for i in range(1): #instantiate N cells
    cell = Cell_3()
    cells_3.append(cell)

cells_4 = []
for i in range(2): #instantiate N cells
    cell = Cell_4()
    cells_4.append(cell)
    rects.append(cell)

cells_5 = []
for i in range(2): #instantiate N cells
    cell = Cell_5()
    cells_5.append(cell)
    rects.append(cell)


driver = Grab_driver()

running = True

while running:
    warm_col = (255, random.randint(0, 255), 0)
    surface.fill(black)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            # upon closing the window with mouse 
            running = False 

    driver.wander()
    driver.draw() 
        
    for npc in cells_1: 
        npc.wander()
        npc.draw()

    for npc in cells_2: 
        npc.wander()
        npc.draw()

    for npc in cells_3: 
        smoker = npc
        smoker.draw() 

    for npc in cells_4:
        npc.wander() 
        npc.draw() 

    for npc in cells_5: 
        npc.wander()
        npc.draw() 

    (mX, mY) = pygame.mouse.get_pos()
    char1 = pygame.transform.scale(char1, (cellsize-10, cellsize+20))
    mouse_rect = char1.get_rect(center = (mX, mY)) # create rect from surface 
    surface.blit(char1, (mX, mY))

    # compare collisions with mouse, drivers and smokers 
    driver.rect.x = round(driver.x)
    driver.rect.y = round(driver.y)
    smoker.rect.x = round(smoker.x) 
    smoker.rect.y = round(smoker.y)
    for rectangle in rects:
        rectangle.rect.x = round(rectangle.x)
        rectangle.rect.y = round(rectangle.y)

        if rectangle.rect.colliderect(driver.rect) or rectangle.rect.colliderect(mouse_rect) or rectangle.rect.colliderect(smoker.rect): 
            rectangle.x_speed *= -1 
            rectangle.y_speed *= -1 

    for i in range(len(rects)): 
        for j in range(i+1, len(rects)): # compare with all elements in the for loop 
            rects[i].rect.x = round(rects[i].x)
            rects[i].rect.y = round(rects[i].y)
            rects[j].rect.x = round(rects[j].x)
            rects[j].rect.y = round(rects[j].y)
            
            if rects[i].rect.colliderect(rects[j]):
                rects[i].x_speed *= -1 
                rects[i].y_speed *= -1 

    for row in range(rows): 
        for col in range(cols): 
            for i in rects: 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 


    for row in range(rows): 
        for col in range(cols): 
            for i in cells_1: 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 

    for row in range(rows): 
        for col in range(cols): 
            for i in cells_2: 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3) 
                    
    for row in range(rows): 
        for col in range(cols): 
            for i in cells_3:  # SMOKERS 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, bright_red, (x,y), 3) 
                    
    for row in range(rows): 
        for col in range(cols): 
            for i in cells_4: 
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(i.x, i.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3)   

    for row in range(rows): 
        for col in range(cols):  
                    x = col * cellsize + padding
                    y = row * cellsize + padding 
                    within_dist = euclid_dist(mX, mY, x, y)
                    npc_within = euclid_dist(driver.x, driver.y, x, y) 

                    if within_dist == True or npc_within == True:
                        pygame.draw.circle(surface, warm_col, (x,y), 3)   

              

    pygame.display.update() 
    pygame.time.Clock().tick(fps) 
    pygame.mouse.set_visible(False) 

pygame.quit()
