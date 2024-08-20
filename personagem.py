import pygame

import time

import inimigos

import tiro

class Jogador(pygame.sprite.Sprite):
    def __init__(self, velocidade:int , vida:int, forca:int):
        super().__init__()
        self.tamanho = (30, 30)
        self.velocidade = velocidade/2
        self.vida = vida*5
        self.forca = forca
        self.imagem = ""
        self.x = 900
        self.y = 400
        self.podeAtaque = 1
        self.podeAtirar = 1
        self.podePassiva = 1
        self.podeDanoArea = 1
        self.tempoAtaque = 0
        self.tempoPassiva = 0
        self.tempoTiro = 0
        self.tempoDanoArea = 0
        self.h = 0
        self.v = 0
        self.lastv = 0
        self.lasth = 0
        self.rect = pygame.Rect((800 , 250), self.tamanho)

    def atualizaPosicao(self, x:int, y:int):
        self.rect.x += self.velocidade * x
        self.rect.y += self.velocidade * y
    
    def desenhar_jogador(self, cor: tuple, tela):
        pygame.draw.rect(tela, cor, self.rect)
        
    def danoArea(self, janela):
        if time.time() - self.tempoDanoArea > 15:
            return
        else:
            self.tempoDanoArea = time.time()
            dano_em_area = pygame.Rect(self.rect.x-50, self.rect.y-50, 130, 130)
            pygame.draw.rect(janela, (255,0,0), dano_em_area)    
            pygame.draw.rect(janela, (0,0,0), self.rect)
    
    def atirar(self, tiros: list):
        if time.time() - self.tempoTiro > 15:
            return
        else:
            if self.v == 0 and self.h == 0:
                tiros.append(tiro.Tiro(self.rect.x, self.rect.y, self.lastv/2, self.lasth/2))
            else:
                tiros.append(tiro.Tiro(self.rect.x, self.rect.y, self.v/2, self.h/2))

    def bater(self, janela):
        if self.v == 0 and self.h == 0:
            golpe = pygame.Rect(self.rect.x+(30*self.lasth/2), self.rect.y+(30*self.lastv/2), 30, 30)
        #personagem dando porrada andando
        else:
            golpe = pygame.Rect(self.rect.x+(30*self.h/2), self.rect.y+(30*self.v/2), 30, 30)
            pygame.draw.rect(janela, (0,0,255), golpe)
    
    def movimentar(self, v: int, h:int):
        #pra cima
        if v == -1:
            self.rect.y -= self.velocidade
            self.lastv = 1
        #pra baixo
        if v == 1:
            self.rect.y += self.velocidade
            self.lastv = -1
        #pra esquerda
        if h == -1:
            self.rect.x -= self.velocidade
            self.lasth = 1
        #pra direita
        if h == 1:
            self.rect.x += self.velocidade
            self.lasth = -1
            
    # correcoes com a parede
    def corrigirPosicao(self):
        #direita parte de baixo
        if(self.rect.x + 30 >= 1151 and self.rect.y>= 265):
            self.rect.x -= 2
        #direita parte de cima
        if (self.rect.x + 30 >= 1021 and self.rect.y < 265):
            self.rect.x -=2
        #esquerda parte de baixo
        if self.rect.x <= 102 and self.rect.y >= 265:
            self.rect.x += 2
        #esquerda em cima
        if self.rect.x <= 229 and self.rect.y < 265:
            self.rect.x +=2
        #em cima
        if self.rect.y < 121 and self.rect.x > 229 and self.rect.x < 1021:
            self.rect.y +=2
        #cima baixo
        if self.rect.y < 267 and (self.rect.x <= 229 or self.rect.x >= 1021):
            self.rect.y +=2
        #embaixo
        if self.rect.y + 30 >= 600:
            self.rect.y = 569

    def ultimoMovimento(self, lasth: int, lastv: int):
        self.lasth = lasth
        self.lastv = lastv

    
        
class Atirador(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 2
        self.danoDist = 5
        self.danoAreax = 2
    def passiva(self):
        self.danoSoco = 5


class Mago(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 3
        self.danoDist = 4
        self.danoAreax = 3 
    def passiva(self):
        self.vida += 10


class Tanque(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 5
        self.danoDist = 2
        self.danoAreax = 3
    def passiva(self):
        self.danoAreax = 5


class Assassino(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 4
        self.danoDist = 3
        self.danoAreax = 4
    def passiva(self):
        self.danoSoco = 6



