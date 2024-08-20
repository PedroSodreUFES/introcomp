import pygame

import random

import personagem

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(300, 600), random.randint(200, 400), 30, 30)
        self.velocidade = 1.5
        self.vida = 7

    def andar(self, jogador):
        if jogador.rect.x > self.rect.x:
            self.rect.x += self.velocidade
        elif jogador.rect.x < self.rect.x:
            self.rect.x -= self.velocidade
        if jogador.rect.y > self.rect.y:
            self.rect.y += self.velocidade
        elif jogador.rect.y < self.rect.y:
            self.rect.y -= self.velocidade

    # correcoes com a parede
    def corrigirPosicao(self):
        #direita parte de baixo
        if(self.rect.x + 30 >= 1151 and self.rect.y>= 265):
            self.rect.x -= self.velocidade
        #direita parte de cima
        if (self.rect.x + 30 >= 1021 and self.rect.y < 265):
            self.rect.x -= self.velocidade
        #esquerda parte de baixo
        if self.rect.x <= 102 and self.rect.y >= 265:
            self.rect.x += self.velocidade
        #esquerda em cima
        if self.rect.x <= 229 and self.rect.y < 265:
            self.rect.x += self.velocidade
        #em cima
        if self.rect.y < 121 and self.rect.x > 229 and self.rect.x < 1021:
            self.rect.y += self.velocidade
        #cima baixo
        if self.rect.y < 267 and (self.rect.x <= 229 or self.rect.x >= 1021):
            self.rect.y += self.velocidade
        #embaixo
        if self.rect.y + 30 >= 600:
            self.rect.y = 569

    def desenhaInimigo(self, janela, cor):
        pygame.draw.rect(janela, cor, self.rect)

    def darDano(self, jogador):
        if self.rect.colliderect(jogador.rect):
            jogador.vida -= 0.1

