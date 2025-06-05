import pygame
from zombie_1 import Zombie
from player import Player
from tree import Tree
from barrier import Barrier

pygame.init()

# Setup
info = pygame.display.Info()
window_width = info.current_w
window_height = info.current_h
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("TheLastTree")
clock = pygame.time.Clock()
running = True

# Load assets
tree_image = pygame.image.load("TheLastTree/code/assets/tree/tree.png").convert_alpha()

sprite_sheets = {
    "down": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_down.png").convert_alpha(),
    "up": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_up.png").convert_alpha(),
    "left": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_left_down.png").convert_alpha(),
    "right": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_right_down.png").convert_alpha(),
    "left_up": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_left_up.png").convert_alpha(),
    "left_down": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_left_down.png").convert_alpha(),
    "right_up": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_right_up.png").convert_alpha(),
    "right_down": pygame.image.load("TheLastTree/code/assets/character/Walk/walk_right_down.png").convert_alpha(),
}

# Sprite groups
all_sprites = pygame.sprite.Group()
barriers = pygame.sprite.Group()

# Create tree
tree = Tree(all_sprites, tree_image, position=(window_width // 2, window_height // 2), scale=1.5)

# Create an invisible barrier covering the tree's base area
barrier_rect = pygame.Rect(
    tree.rect.centerx - 42,  # half of tree width (85 / 2)
    tree.rect.bottom - 40,   # near base of tree
    84,                      # full width
    40                       # reasonable trunk area height
)
barrier = Barrier([all_sprites, barriers], barrier_rect)


# Create characters
zombie1 = Zombie(all_sprites, window_width, window_height, sprite_sheets["up"], tree.rect, barriers)
player = Player(all_sprites, window_width, window_height, sprite_sheets, barriers)

# Game loop
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgrey")
    all_sprites.update(dt)
    all_sprites.draw(screen)
    pygame.display.flip()
