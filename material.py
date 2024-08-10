import pygame

pygame.init()

img_fundo = pygame.image.load("imagens/fundo.jpg")

img_botao = pygame.image.load("imagens/botao.webp")
img_botao = pygame.transform.scale(img_botao, (280, 60))
rect_botao = img_botao.get_rect()

img_seta = pygame.image.load("imagens/seta.png")
img_seta = pygame.transform.scale_by(img_seta, 0.1)
img_seta = pygame.transform.rotate(img_seta, -90)
rect_seta = img_seta.get_rect()
rect_seta.x = 100

posicoes_seta = [90, 160, 230, 300]
pos_atual_seta = 0
largura = 626
altura = 394
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Menu do Introcomp')

fps = 60
clock = pygame.time.Clock()
main_menu = False
fonte = pygame.font.Font('freesansbold.ttf', 32)
menu_controle = -1

class Buttons:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 260, 40)

    def draw(self, tela):
        tela.blit(img_botao, self.button)
        text = fonte.render(self.text, True,(0, 0, 0))  # temos um anti-aliasing aqui, mas nao precisamos nos preocupar com isso
        tela.blit(text, (self.pos[0] + 20, self.pos[1] + 15))  # mudar aqui depois se precisar

    def checa_clique(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


def desenha_jogo():
    button = Buttons('Menu Principal', (340, 325))
    button.draw(tela)

    return button.checa_clique()


def desenha_menu_principal():

    pygame.draw.rect(tela, (0, 0, 0), [163, 64, 300, 299])
    botao_menu = Buttons('Sair do Menu', (173, 290))
    notebook_aula = Buttons('Notebook', (173, 80))
    feedback = Buttons('Feedback', (173, 150))
    equipe = Buttons('Equipe', (173, 220))
    
    botao_menu.draw(tela)
    notebook_aula.draw(tela)
    feedback.draw(tela)
    equipe.draw(tela)

run = True
while run:
    tela.blit(img_fundo, (0,0))
    clock.tick(fps)

    if main_menu:
        desenha_menu_principal()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pos_atual_seta+=1
                    if pos_atual_seta > 3 :
                        pos_atual_seta = 3
                elif event.key == pygame.K_UP:
                    pos_atual_seta-=1
                    if pos_atual_seta < 0 :
                        pos_atual_seta = 0
                elif event.key == pygame.K_RETURN:
                    main_menu = False
        rect_seta.y = posicoes_seta[pos_atual_seta]
        menu_controle = pos_atual_seta
        tela.blit(img_seta, rect_seta)
    else:
        main_menu = desenha_jogo()
        if menu_controle == 0:
            text = fonte.render('Introcomp.com/Notebook', True, (0, 0, 0))
            tela.blit(text, (120, 150))
        if menu_controle == 1:
            text = fonte.render('Introcomp.com/Feedback', True, (0, 0, 0))
            tela.blit(text, (120, 150))
        if menu_controle == 2:
            text = fonte.render('Introcomp.com/Equipe', True, (0, 0, 0))
            tela.blit(text, (120, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()