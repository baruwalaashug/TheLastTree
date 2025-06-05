import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, groups, rect):
        super().__init__(groups)
        self.image = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # Invisible
        self.rect = rect
