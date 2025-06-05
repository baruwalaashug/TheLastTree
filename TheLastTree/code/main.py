import pygame
from zombie_1 import Zombie
from player import Player

pygame.init()

# Constants
info = pygame.display.Info()
window_width = info.current_w
window_height = info.current_h
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("TheLastTree")
screen = pygame.display.set_mode((window_width, window_height))

# Load assets
tree_image = pygame.image.load("TheLastTree/code/assets/tree/Trees.png").convert_alpha()
tree_rect = tree_image.get_rect(center=(window_width / 2, window_height / 3))
character_image = pygame.image.load("TheLastTree/code/assets/character/idle/idle_down.png").convert_alpha()

# Sprite groups and game objects
all_sprites = pygame.sprite.Group()
zombie1 = Zombie(all_sprites, window_width, window_height, character_image, tree_rect)
player = Player(all_sprites, window_width, window_height, character_image)

# Game loop
while running:
    dt = clock.tick(60) / 1000  # Time delta in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgrey")
    screen.blit(tree_image, tree_rect)
    all_sprites.update(dt)
    all_sprites.draw(screen)
    pygame.display.flip()