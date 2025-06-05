import pygame
import random
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
zombie_group = pygame.sprite.Group()

# Create tree slightly above center
tree_y_offset = 100
tree = Tree(
    all_sprites,
    tree_image,
    position=(window_width // 2, window_height // 2 - tree_y_offset),
    scale=1.5
)

# Create barrier around tree
barrier_rect = pygame.Rect(0, 0, 90, 112)
barrier_rect.center = tree.rect.center
barrier = Barrier([all_sprites, barriers], barrier_rect)

# Create player (spawned below the tree)
player_spawn_offset = 150
player = Player(all_sprites, window_width, window_height, sprite_sheets, barriers, zombie_group)
player.rect.centery += player_spawn_offset

# Wave system
wave = 1
zombies_per_wave = 5
zombies_spawned = 0
zombie_spawn_interval = 1000
last_zombie_spawn_time = 0
wave_start_time = pygame.time.get_ticks()
time_between_waves = 5000
font = pygame.font.SysFont(None, 48)
countdown_active = False

def get_spawn_position_for_wave(wave, window_width, window_height):
    margin = 50
    if wave == 1:  # from bottom
        return (random.randint(0, window_width), window_height + margin)
    elif wave == 2:  # from left
        return (-margin, random.randint(0, window_height))
    elif wave == 3:  # from right
        return (window_width + margin, random.randint(0, window_height))
    elif wave == 4:  # from top
        return (random.randint(0, window_width), -margin)
    else:
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            return (random.randint(0, window_width), -margin)
        elif side == "bottom":
            return (random.randint(0, window_width), window_height + margin)
        elif side == "left":
            return (-margin, random.randint(0, window_height))
        else:
            return (window_width + margin, random.randint(0, window_height))

# Game loop
while running:
    dt = clock.tick(60) / 1000
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgrey")

    # Handle countdown
    if zombies_spawned >= zombies_per_wave and not zombie_group:
        if not countdown_active:
            countdown_active = True
            wave_start_time = now

        remaining = time_between_waves - (now - wave_start_time)
        if remaining <= 0:
            wave += 1
            zombies_per_wave += 2
            zombies_spawned = 0
            last_zombie_spawn_time = now
            countdown_active = False
        else:
            seconds = remaining // 1000 + 1
            text = font.render(f"Wave {wave + 1} in {seconds}", True, (255, 255, 255))
            screen.blit(text, (20, 20))  # Top-left corner

    # Spawn zombies during wave
    if zombies_spawned < zombies_per_wave and not countdown_active:
        if now - last_zombie_spawn_time >= zombie_spawn_interval:
            spawn_pos = get_spawn_position_for_wave(wave, window_width, window_height)
            is_boss = wave >= 5 and random.random() < 0.2
            zombie = Zombie(all_sprites, spawn_pos, sprite_sheets["up"], tree.rect, barriers, is_boss=is_boss)
            zombie_group.add(zombie)
            zombies_spawned += 1
            last_zombie_spawn_time = now

    # Update and draw
    all_sprites.update(dt)
    tree.damage_if_colliding(zombie_group)
    all_sprites.draw(screen)
    tree.draw_ui(screen)
    pygame.display.flip()
