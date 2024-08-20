import pygame

import random

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.largura = 30
        self.altura = 30
        self.image = pygame.Surface((self.largura, self.altura))
        self.image.fill((255, 0, 0))  # Cor vermelha para o inimigo
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - self.largura)
        self.rect.y = -self.altura
        self.velocidade = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura:
            self.rect.x = random.randint(0, largura - self.largura)
            self.rect.y = -self.altura
            self.velocidade = random.randint(1, 5)
