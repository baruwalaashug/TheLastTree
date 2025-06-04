import pygame

pygame.init()

class Zombie(pygame.sprite.Sprite):
    
    def __init__(self, groups, window_width, window_height, sprite):
        super().__init__(groups)
        self.image = sprite 
        self.rect = self.image.get_rect(center = (window_width / 2, window_height / 2))

    def update(self):
        pass