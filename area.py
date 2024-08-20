import pygame

class Area(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__
        self.rect = pygame.Rect(x, y, 120, 90)
    def drawArea(self, janela, cor):
        pygame.draw.rect(janela, cor, self.rect)
