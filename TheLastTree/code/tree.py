import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self, groups, image, position, scale=1):
        super().__init__(groups)

        # Scale if requested
        if scale != 1:
            width = int(image.get_width() * scale)
            height = int(image.get_height() * scale)
            image = pygame.transform.scale(image, (width, height))

        self.image = image
        self.rect = self.image.get_rect(center=position)
