import pygame

class geral(pygame.sprite.Sprite):
    super().__init__()
    def __init__(self, vida, ataque, defesa, velocidade):
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.congelado = 0
        self.pegandofogo = 0
        self.joga = 1 # diz se o personagem pode jogar nessa rodada
        self.skillAvailable = 1 # diz se o personagem pode usar sua habilidade