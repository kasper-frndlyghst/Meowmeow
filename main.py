import pygame 
from pygame.locals import *


pygame.init()
#CONSTANTS
vec = pygame.math.Vector2
height = 800
width = 1300 
accel = 1
grav = 0.5
friction = -0.1
frame_rate = 60

fatherTime = pygame.time.Clock()

#VARIABLES
shit_the_bed = False

#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cat.png")
        self.surf = pygame.Surface ((30, 50)) #~GOlden ratio, he must be beautiful <3
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 0.90 * height))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

    #And newton said, let there be motion
    def move(self):
        self.acc = vec(0,grav)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[97]:
            self.acc.x = -accel
        if pressed_keys[100]:
            self.acc.x = accel

        #still working on moving
        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + 0.7 *self.acc
        
        #Stuck in the matrix ? :3
        if self.pos.x > width:
            self.pos.x = width
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos

#Lets do some collision detection // I would put this in a class file but this is a proto so no
    def shit_went_down(self):
        hits = pygame.sprite.spritecollide(NYA ,sprites, False)
        if NYA.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((width,20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (width/2, height - (0.02*height)))


STEP = Floor()
NYA = Player()  

#Sprite calling 
sprites = pygame.sprite.Group()
sprites.add(STEP)
sprites.add(NYA)
      

sprites = pygame.sprite.Group()
sprites.add(STEP)
sprites.add(NYA)

myEyes = pygame.display.set_mode((width,height))
pygame.display.set_caption('Cats are from hell')


while not shit_the_bed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shit_the_bed = True

        print(f"Lookie here you fucking did it \n this( {event} ) shit really happened")
    myEyes.fill((0,0,0))
    

    for thing in sprites:
        myEyes.blit(thing.surf, thing.rect)

    NYA.move()
    NYA.shit_went_down()
    pygame.display.update()
    fatherTime.tick(frame_rate)



pygame.quit()
quit()

