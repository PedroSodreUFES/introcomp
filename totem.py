import pygame

class Totem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 580
        self.y = 320
        self.vida = 100
        self.rect= pygame.Rect(self.x, self.y, 100, 100)
    def desenhaTotem(self, janela, cor):
        pygame.draw.rect(janela, cor, self.rect)
        fonte = pygame.font.Font("freesansbold.ttf", 36)
        text = fonte.render("T", True, (255,255,255))
        janela.blit(text, (620, 355))
