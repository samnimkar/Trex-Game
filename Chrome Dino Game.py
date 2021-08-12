import pygame

# Initilization
pygame.init()

# sets how large the GUI (or window/screen) will be - adjust if needed
windowX = 960
windowY = 720
window = pygame.display.set_mode((windowX,windowY))

pygame.display.set_caption("Dino Run - Alternate Dimensions")

# displays window
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False