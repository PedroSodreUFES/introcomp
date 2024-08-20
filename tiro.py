import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, vertical: int, horizontal: int):
        super().__init__()
        self.x = x
        self.y = y
        self.vertical = vertical
        self.horizontal = horizontal
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
    def desenha(self, color: tuple , tela):
        pygame.draw.rect(tela, color, self.rect)
    def atualiza(self):
        self.x += 5*self.horizontal
        self.y += 5*self.vertical
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
    def removeTiro(self):
        if self.x <= 0 or self.x >= 1280 or self.y <= 0 or self.y >= 720:
            return True
        else:
            return False