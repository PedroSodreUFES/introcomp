import pygame

import time

import totem

import enemy

import tiro

class Jogador(pygame.sprite.Sprite):
    def __init__(self, velocidade:int , vida:int, forca:int):
        super().__init__()
        self.tamanho = (30, 30)
        self.velocidade = velocidade/2
        self.vida = vida*5
        self.vidaTotal = vida*5
        self.forca = forca
        self.imagem = ""
        self.podeAtaque = 1
        self.podeAtirar = 1
        self.podePassiva = 1
        self.podeDanoArea = 1
        self.tempoPassiva = time.time()
        self.tempoTiro = time.time()
        self.tempoDanoArea = time.time()
        self.h = 0
        self.v = 0
        self.lastv = 0
        self.lasth = 0
        self.rect = pygame.Rect((300 , 200), self.tamanho)
        self.colidiuArea = 0
        self.passivaTime = 0

    def atualizaPosicao(self, x:int, y:int):
        self.rect.x += self.velocidade * x
        self.rect.y += self.velocidade * y
    
    def desenhar_jogador(self, cor: tuple, tela):
        pygame.draw.rect(tela, cor, self.rect)
        
    
    def atirar(self, tiros: list, v: int, h: int, lastv:int, lasth: int):
        if time.time() - self.tempoTiro < 2:
            return
        else:
            self.tempoTiro = time.time()
            if v == 0 and h == 0:
                tiros.append(tiro.Tiro(self.rect.x, self.rect.y, lastv, lasth))
            else:
                tiros.append(tiro.Tiro(self.rect.x, self.rect.y, v, h))
    
    def movimentar(self, v: int, h:int):
        #pra cima
        if v == -1:
            self.rect.y -= self.velocidade
            self.lastv = 1
            self.lasth = 0
        #pra baixo
        if v == 1:
            self.rect.y += self.velocidade
            self.lastv = -1
            self.lasth = 0
        #pra esquerda
        if h == -1:
            self.rect.x -= self.velocidade
            self.lasth = 1
            self.lastv = 0
        #pra direita
        if h == 1:
            self.rect.x += self.velocidade
            self.lasth = -1
            self.lastv = 0

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

    def ultimoMovimento(self, lasth: int, lastv: int):
        self.lasth = lasth
        self.lastv = lastv

    
        
class Atirador(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 2
        self.danoDist = 5
        self.danoAreax = 2
    
    def danoArea(self, janela, inimigos: list, toten: totem.Totem):
        if time.time() - self.tempoDanoArea < 5:
            return
        else:
            self.tempoDanoArea = time.time()
            dano_em_area = pygame.Rect(self.rect.x-50, self.rect.y-50, 130, 130)
            pygame.draw.rect(janela, (0,0,255), dano_em_area)    
            pygame.draw.rect(janela, (0,0,0), self.rect)
            for inimigo in inimigos:
                if dano_em_area.colliderect(inimigo.rect):
                    inimigo.vida-= self.danoAreax
                if inimigo.vida <= 0:
                    inimigos.pop(inimigos.index(inimigo))
            if dano_em_area.colliderect(toten.rect):
                toten.vida -= self.danoAreax 
    
    def bater(self, janela, v: int, h: int, lasth:int, lastv: int, inimigos: list, toten: totem.Totem ):
        #personagem dando soco parado
        if v == 0 and h == 0:
            golpe = pygame.Rect(self.rect.x+(30*lasth), self.rect.y+(30*lastv), 30, 30)
        #personagem dando soco andando
        else:
            golpe = pygame.Rect(self.rect.x+(30*h), self.rect.y+(30*v), 30, 30)
            pygame.draw.rect(janela, (0,0,255), golpe)
        for inimigo in inimigos:
            if golpe.colliderect(inimigo.rect):
                inimigo.vida-= self.danoSoco
            if inimigo.vida <= 0:
                inimigos.pop(inimigos.index(inimigo))
        if golpe.colliderect(toten.rect):
            toten.vida -= self.danoSoco

    def passiva(self):
        if time.time() - self.tempoPassiva < 40:
            return
        else:
            self.tempoPassiva = time.time()
            self.danoDist = 10

    def desativaPassiva(self):
        if time.time() - self.tempoPassiva > 15:
            self.danoSoco = 5


class Mago(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 3
        self.danoDist = 4
        self.danoAreax = 3 

    def danoArea(self, janela, inimigos: list, toten: totem.Totem):
        if time.time() - self.tempoDanoArea < 5:
            return
        else:
            self.tempoDanoArea = time.time()
            dano_em_area = pygame.Rect(self.rect.x-50, self.rect.y-50, 130, 130)
            pygame.draw.rect(janela, (0,0,255), dano_em_area)    
            pygame.draw.rect(janela, (0,0,0), self.rect)
            for inimigo in inimigos:
                if dano_em_area.colliderect(inimigo.rect):
                    inimigo.vida-= self.danoAreax
                if inimigo.vida <= 0:
                    inimigos.pop(inimigos.index(inimigo))
            if dano_em_area.colliderect(toten.rect):
                toten.vida -= self.danoAreax 
            

    def passiva(self):
        if time.time() - self.tempoPassiva < 40:
            return
        else:
            self.tempoPassiva = time.time()
            self.vida += 30
    
    def desativaPassiva(self):
        if time.time() - self.tempoPassiva > 15:
            self.danoSoco = 3
    

    def bater(self, janela, v: int, h: int, lasth:int, lastv: int, inimigos: list, toten: totem.Totem ):
        #personagem dando soco parado
        if v == 0 and h == 0:
            golpe = pygame.Rect(self.rect.x+(30*lasth), self.rect.y+(30*lastv), 30, 30)
        #personagem dando soco andando
        else:
            golpe = pygame.Rect(self.rect.x+(30*h), self.rect.y+(30*v), 30, 30)
            pygame.draw.rect(janela, (0,0,255), golpe)
        for inimigo in inimigos:
            if golpe.colliderect(inimigo.rect):
                inimigo.vida-= self.danoSoco
            if inimigo.vida <= 0:
                inimigos.pop(inimigos.index(inimigo))
        if golpe.colliderect(toten.rect):
            toten.vida -= self.danoSoco



class Tanque(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 5
        self.danoDist = 2
        self.danoAreax = 3
    
    def danoArea(self, janela, inimigos: list, toten: totem.Totem):
        if time.time() - self.tempoDanoArea < 5:
            return
        else:
            self.tempoDanoArea = time.time()
            dano_em_area = pygame.Rect(self.rect.x-50, self.rect.y-50, 130, 130)
            pygame.draw.rect(janela, (0,0,255), dano_em_area)    
            pygame.draw.rect(janela, (0,0,0), self.rect)
            for inimigo in inimigos:
                if dano_em_area.colliderect(inimigo.rect):
                    inimigo.vida-= self.danoAreax
                if inimigo.vida <= 0:
                    inimigos.pop(inimigos.index(inimigo))
            if dano_em_area.colliderect(toten.rect):
                toten.vida -= self.danoAreax 

    def bater(self, janela, v: int, h: int, lasth:int, lastv: int, inimigos: list, toten: totem.Totem ):
        #personagem dando soco parado
        if v == 0 and h == 0:
            golpe = pygame.Rect(self.rect.x+(30*lasth), self.rect.y+(30*lastv), 30, 30)
        #personagem dando soco andando
        else:
            golpe = pygame.Rect(self.rect.x+(30*h), self.rect.y+(30*v), 30, 30)
            pygame.draw.rect(janela, (0,0,255), golpe)
        for inimigo in inimigos:
            if golpe.colliderect(inimigo.rect):
                inimigo.vida-= self.danoSoco
            if inimigo.vida <= 0:
                inimigos.pop(inimigos.index(inimigo))
        if golpe.colliderect(toten.rect):
            toten.vida -= self.danoSoco

    def passiva(self):
        if time.time() - self.tempoPassiva < 40:
            return
        else:
            self.tempoPassiva = time.time()
            self.danoAreax = 10

    def desativaPassiva(self):
        if time.time() - self.tempoPassiva > 15:
            self.danoAreax = 3


class Assassino(Jogador):
    def __init__(self, velocidade:int, vida:int, forca:int):
        super().__init__(velocidade, vida, forca)
        self.danoSoco = 4
        self.danoDist = 3
        self.danoAreax = 4
    
    def danoArea(self, janela, inimigos: list, toten: totem.Totem):
        if time.time() - self.tempoDanoArea < 5:
            return
        else:
            self.tempoDanoArea = time.time()
            dano_em_area = pygame.Rect(self.rect.x-50, self.rect.y-50, 130, 130)
            pygame.draw.rect(janela, (0,0,255), dano_em_area)    
            pygame.draw.rect(janela, (0,0,0), self.rect)
            for inimigo in inimigos:
                if dano_em_area.colliderect(inimigo.rect):
                    inimigo.vida-= self.danoAreax
                if inimigo.vida <= 0:
                    inimigos.pop(inimigos.index(inimigo))
            if dano_em_area.colliderect(toten.rect):
                toten.vida -= self.danoAreax 
    
    
    def passiva(self):
        if time.time() - self.tempoPassiva < 40:
            return
        else:
            self.tempoPassiva = time.time()
            self.danoSoco = 6
    
    def desativaPassiva(self):
        if time.time() - self.tempoPassiva > 15:
            self.danoSoco = 4

    def bater(self, janela, v: int, h: int, lasth:int, lastv: int, inimigos: list, toten: totem.Totem ):
        #personagem dando soco parado
        if v == 0 and h == 0:
            golpe = pygame.Rect(self.rect.x+(30*lasth), self.rect.y+(30*lastv), 30, 30)
        #personagem dando soco andando
        else:
            golpe = pygame.Rect(self.rect.x+(30*h), self.rect.y+(30*v), 30, 30)
            pygame.draw.rect(janela, (0,0,255), golpe)
        for inimigo in inimigos:
            if golpe.colliderect(inimigo.rect):
                inimigo.vida-= self.danoSoco
            if inimigo.vida <= 0:
                inimigos.pop(inimigos.index(inimigo))
        if golpe.colliderect(toten.rect):
            toten.vida -= self.danoSoco