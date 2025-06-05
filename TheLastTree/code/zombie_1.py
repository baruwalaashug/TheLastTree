import pygame
import math

class Zombie(pygame.sprite.Sprite):
    def __init__(self, groups, window_width, window_height, sprite_sheet, target):
        super().__init__(groups)

        self.frames = []
        self.load_frames(sprite_sheet)
        self.current_frame = 0
        self.animation_distance_threshold = 10  # pixels before advancing frame
        self.distance_moved = 0

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(midbottom=(window_width / 2, window_height))
        
        self.target = target.center
        self.speed = 1
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
        current_x, current_y = self.rect.center
        target_x, target_y = self.target

        dx = target_x - current_x
        dy = target_y - current_y
        distance = math.hypot(dx, dy)

        if distance > 0:
            dx /= distance
            dy /= distance

        if distance > self.speed:
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

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
