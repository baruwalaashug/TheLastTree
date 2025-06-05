import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, window_width, window_height, sprite_sheet):
        super().__init__(groups)

        self.frames = []
        self.load_frames(sprite_sheet)
        self.current_frame = 0
        self.animation_distance_threshold = 10  # pixels before advancing frame
        self.distance_moved = 0

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(window_width / 2, window_height / 2))

        self.speed = 200  # pixels per second
        self.last_pos = pygame.math.Vector2(self.rect.x, self.rect.y)

    def load_frames(self, sprite_sheet):
        def get_image(sheet, frame, width, height, scale, colour):
            image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
            image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
            image = pygame.transform.scale(image, (width * scale, height * scale))
            image.set_colorkey(colour)
            return image

        BLACK = (0, 0, 0)
        for i in range(8):
            self.frames.append(get_image(sprite_sheet, i, 45, 45, 1, BLACK))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        move_x = (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed * dt
        move_y = (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed * dt

        self.rect.x += move_x
        self.rect.y += move_y

        current_pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        moved = current_pos.distance_to(self.last_pos)
        self.distance_moved += moved
        self.last_pos = current_pos

        if self.distance_moved >= self.animation_distance_threshold:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.distance_moved = 0
        elif moved == 0:
            self.image = self.frames[0]
