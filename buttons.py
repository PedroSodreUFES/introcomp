import pygame

img_botao = pygame.image.load("./imagens/botao.png")
img_botao = pygame.transform.scale_by(img_botao, 1.8)

class Buttons:
    def __init__(self, text: str, pos: tuple):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 300, 100)
        self.fonte =  pygame.font.Font('freesansbold.ttf', 18)
    
    def draw(self, tela):
        tela.blit(img_botao, self.button)
        text = self.fonte.render(self.text, True, (255,255,255))
        tela.blit(text, (self.pos[0]+40, self.pos[1]+32))
        
    def checa_clique(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False