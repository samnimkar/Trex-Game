import pygame
import os

from pygame.color import Color

# Initilization
pygame.init()

# sets how large the GUI (or window/screen) will be - adjust if needed
windowX = 960
windowY = 720
window = pygame.display.set_mode((windowX,windowY))

pygame.display.set_caption("Dino Run - Alternate Dimensions")

# import background images - will change for new levels
track = pygame.image.load(os.path.join('Assets/Other', 'Track.png'))
cloud = pygame.image.load(os.path.join('Assets/Other', 'Cloud.png'))
bird = [pygame.image.load(os.path.join('Assets/Bird', 'Bird1.png')),
        pygame.image.load(os.path.join('Assets/Bird', 'Bird2.png'))]
cactus = [pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus1.png')),
        pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus2.png')),
        pygame.image.load(os.path.join('Assets/Cactus', 'LargeCactus3.png')),
        pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus1.png')),
        pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus2.png')),
        pygame.image.load(os.path.join('Assets/Cactus', 'SmallCactus3.png'))]

# import dino images - will change for new levels
dino = [pygame.image.load(os.path.join('Assets/Dino', 'DinoDead.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck1.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoDuck2.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoJump.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoRun1.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoRun2.png')),
        pygame.image.load(os.path.join('Assets/Dino', 'DinoStart.png'))]

# need to create if statement to set diff colours on level
backGroundColour = (255,255,255)        #RGB for white
window.fill(backGroundColour)
window.blit(track,(0*(windowX),0.75*(windowY))) #put track on GUI

#set class for dino and program motion

# displays window
pygame.display.flip()

running = True
while running:
  pygame.Surface
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False