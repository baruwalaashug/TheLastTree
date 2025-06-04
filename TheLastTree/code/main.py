#imports
import pygame
from zombie_1 import Zombie
from player import Player

pygame.init()

# constants
info = pygame.display.Info()
window_width = info.current_w
window_height = info.current_h
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("TheLastTree")
screen = pygame.display.set_mode((window_width, window_height))

tree_image = pygame.image.load("TheLastTree/code/assets/tree/Trees.png").convert_alpha()
tree_rect = tree_image.get_rect(center = (window_width / 2, window_height / 3))


#sprites
character_image = pygame.image.load("TheLastTree/code/assets/character/idle/idle_down.png").convert_alpha()
all_sprite = pygame.sprite.Group()
zombie1 = Zombie(all_sprite, window_width, window_height, character_image, tree_rect)
player = Player(all_sprite, window_width, window_height, character_image)

#Segment sprite sheet
BLACK=(0,0,0)
def get_image(character_image,frame, width, height, scale, colour):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(character_image, (0, 0), ((frame*width),0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)
    return image


frame_0= get_image(character_image,0, 45 ,45, 1, BLACK)
frame_1= get_image(character_image,1, 45 ,45, 1, BLACK)
frame_2= get_image(character_image,2, 45 ,45, 1, BLACK)
frame_3= get_image(character_image,3, 45 ,45, 1, BLACK)
frame_4= get_image(character_image,4, 45 ,45, 1, BLACK)
frame_5= get_image(character_image,5, 45 ,45, 1, BLACK)
frame_6= get_image(character_image,6, 45 ,45, 1, BLACK)
frame_7= get_image(character_image,7, 45 ,45, 1, BLACK)

#show frame image
screen.blit(frame_0, (0, 0))
screen.blit(frame_1, (45, 0))
screen.blit(frame_2, (90, 0))
screen.blit(frame_3, (135, 0))
screen.blit(frame_4, (180, 0))
screen.blit(frame_5, (225, 0))
screen.blit(frame_6, (270, 0))
screen.blit(frame_7, (315, 0))

#game loop
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("darkgrey")
  screen.blit(frame_0, (0, 0)) #show frame image
  screen.blit(tree_image, tree_rect)
  all_sprite.draw(screen)
  all_sprite.update()
 
  pygame.display.flip()
