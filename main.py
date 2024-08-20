import pygame

import random

import aux

from buttons import Buttons

import tiro

import totem

import area

import time

import personagem

pygame.init()

#settings janela 
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))
fps = 60
clock = pygame.time.Clock()

#telas de fundo
img_fundo = pygame.image.load("imagens/pagina_de_jogar.png")
historinha = pygame.image.load("imagens/historia.png")

#textos de fundo
fonte = pygame.font.Font("freesansbold.ttf", 36)
text = fonte.render("Escolha o numero de jogadores", True, (255,255,255))
fonte = pygame.font.Font("freesansbold.ttf", 28)
text2 = fonte.render("Aperte enter para confirmar e use as setas para escolher", True, (255, 255, 255))

#mapas
map_list =["imagens/mapa0.png" , "imagens/mapa1.png", "imagens/mapa2.png" , "imagens/mapa3.png"]
indice_mapa = random.randint(0, 3)
img_mapa = pygame.image.load(map_list[indice_mapa])

#musica
pygame.mixer_music.load("audios/audio_menu.wav")
pygame.mixer_music.play(-1)

#botoes
um_jogador = Buttons("1 Jogador", (470, 380))
dois_jogadores = Buttons("2 jogadores", (650, 380))

#configuracoes iniciais
executando = True
tela = 1 # 1 = inicio, #2 = escolher personagem #3 = jogo #4 = game over
njogadores = 0
njogadores_selecionados = 0
posicao_seta = 0
venceu = 0
golpe_mouse = True

#carregar seta
seta = pygame.image.load("imagens/seta.png")
seta = pygame.transform.scale_by(seta, 0.5)
seta2 = pygame.image.load("imagens/seta_para_cima.png")

#jogadores
jogador1 = ""
op1 = ""
jogador2 = ""
op2 = ""

#inimigos
inimigos = []

#tiros
tiros = []

#totem
toten = totem.Totem()

#teste movimento
rect = pygame.Rect(100, 100, 30, 30)
x = 100
y = 100
v = 0
h = 0
lasth = 0
lastv = 0

# areas
area1 = area.Area(410, 360)
area2 = area.Area(680, 460)
areas = [area1, area2]

#tempo
inicio = ""


while executando:
    #tela de escolher numero de jogadores
    clock.tick(60)
    if tela == 1:
        janela.blit(img_fundo, (0, 0))
        janela.blit(text, (largura//3.2, 300))
        janela.blit(text2, (280, 340))
        um_jogador.draw(janela)
        dois_jogadores.draw(janela)
        if posicao_seta == 0:
            janela.blit(seta, (430, 410))
        else:
            janela.blit(seta, (820, 410))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    posicao_seta+=1
                    if(posicao_seta > 1):
                        posicao_seta = 0
                    seta =pygame.transform.flip(seta, True, False)
                elif evento.key == pygame.K_LEFT:
                    posicao_seta-=1
                    if posicao_seta < 0:
                        posicao_seta = 1
                    seta =pygame.transform.flip(seta, True, False)
                elif evento.key == pygame.K_RETURN:
                    tela = 2
                    if(posicao_seta == 0):
                        njogadores = 1
                    else:
                        njogadores = 2
                    posicao_seta = 0

    #tela de selecao de personagens            
    elif tela == 2:
        janela.blit(img_fundo, (0, 0))
        aux.desenha_os_cards(janela)
        #DESENHA SETAS
        if posicao_seta == 0:
            janela.blit(seta2, (130, 530))
        elif posicao_seta == 1:
            janela.blit(seta2, (460, 530))
        elif posicao_seta == 2:
            janela.blit(seta2, (765, 530))
        elif posicao_seta == 3:
            janela.blit(seta2, (1080, 530))
        #DESENHA TITULO
        if njogadores == 1 and njogadores_selecionados == 0:
            text = fonte.render("Escolha o seu jogador", True, (255,255,255))
            janela.blit(text, (largura//2.5, 80))
        elif njogadores == 2 and njogadores_selecionados == 0:
            text = fonte.render("Jogador 1 escolhe o jogador", True, (255,255,255))
            janela.blit(text, (largura//2.8, 80))
        elif njogadores == 2 and njogadores_selecionados == 1:
            text = fonte.render("Jogador 2 escolhe o jogador", True, (255,255,255))
            janela.blit(text, (largura//2.8, 80))
        #VE OS EVENTOS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    posicao_seta+=1
                    if(posicao_seta > 3):
                        posicao_seta = 0
                elif evento.key == pygame.K_LEFT:
                    posicao_seta-=1
                    if posicao_seta < 0:
                        posicao_seta = 3
                elif evento.key == pygame.K_RETURN:
                    if njogadores_selecionados == 0:
                        if posicao_seta == 0:
                            jogador1 = personagem.Assassino(8, 10, 2)
                        elif posicao_seta == 1:
                            jogador1 = personagem.Tanque(6, 10, 3)
                        elif posicao_seta == 2:
                            jogador1 = personagem.Atirador(8, 10, 2)
                        elif posicao_seta == 3:
                            jogador1 = personagem.Mago(8, 6, 3)
                    else:
                        if posicao_seta == 0:
                            jogador2 = personagem.Assassino(8, 10, 2)
                        elif posicao_seta == 1:
                            jogador2 = personagem.Tanque(6, 10, 3)
                        elif posicao_seta == 2:
                            jogador2 = personagem.Atirador(8, 10, 2)
                        elif posicao_seta == 3:
                            jogador2 = personagem.Mago(8, 6, 3)
                    njogadores_selecionados+=1
                    if(njogadores == njogadores_selecionados):
                        tela = 3
                        #tempo
                        inicio = time.time()
                elif evento.key == pygame.K_q:
                    janela.blit(historinha, (0,0))
                    text = fonte.render("Pressione Q para sair", True, (255,255,255))
                    janela.blit(text, (largura//2.55, 600))
                    pygame.display.flip()
                    n = True
                    while n == True:
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:
                                n = False
                                executando = False
                                break
                            elif evento.type == pygame.KEYDOWN:
                                if evento.key == pygame.K_q:
                                    n = False
                                    break
    ##########################################################
    ##########################################################
    ##########################################################

        
    #porradaria
    elif tela == 3:
        # se passar de 3 minutos o jogador perde
        if time.time() - inicio > 180:
            tela = 4
        
        #se o totem morrer, o jogo acaba
        #if toten.vida == 0:
           #venceu = 1
            #tela = 4
        
        janela.blit(img_mapa, (0,0))
        toten.desenhaTotem(janela, (0, 200, 0))
        area1.drawArea(janela, (0, 100, 100))
        area2.drawArea(janela, (0, 100, 100))
        jogador1.atualizaPosicao(h, v)
        jogador1.desenhar_jogador((255, 255, 255), janela)
        
        #tiros
        for shot in tiros:
            shot.atualiza()
            if shot.removeTiro():
                tiros.pop(tiros.index(shot))
            shot.desenha((255,0,0), janela)

        #personagens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit() 
            #movimentacao
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    h = -1
                if event.key == pygame.K_RIGHT:
                    h = 1
                if event.key == pygame.K_UP:
                    v = -1
                if event.key == pygame.K_DOWN:
                    v = 1
                #golpe
                if event.key == pygame.K_1:
                    #personagem parado
                    if v == 0 and h == 0:
                        golpe = pygame.Rect(rect.x+(30*lasth/2), rect.y+(30*lastv/2), 30, 30)
                    #personagem dando porrada andando
                    else:
                        golpe = pygame.Rect(rect.x+(30*h/2), rect.y+(30*v/2), 30, 30)
                    pygame.draw.rect(janela, (0,0,255), golpe)
                #atirar
                if event.key == pygame.K_2:
                    if v == 0 and h == 0:
                        tiros.append(tiro.Tiro(rect.x, rect.y, lastv/2, lasth/2))
                    else:
                        tiros.append(tiro.Tiro(rect.x, rect.y, v/2, h/2))
                #dano em área
                if event.key == pygame.K_3:
                    dano_em_area = pygame.Rect(rect.x-50, rect.y-50, 130, 130)
                    pygame.draw.rect(janela, (255,0,0), dano_em_area)    
                    pygame.draw.rect(janela, (0,0,0), rect)
                #passiva
                if event.key == pygame.K_4:
                    pedro = "sodras"
                #golpe pausado 
                if event.key == pygame.K_SPACE:
                    while golpe_mouse == True:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                golpe_mouse = False
                                break
                    golpe_mouse = True

            #movimentacao
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    h = 0
                    jogador1.ultimoMovimento(-1, 0)
                if event.key == pygame.K_RIGHT:
                    h = 0
                    jogador1.ultimoMovimento(1, 0)
                if event.key == pygame.K_UP:
                    v = 0
                    jogador1.ultimoMovimento(0, -1)
                if event.key == pygame.K_DOWN:
                    v = 0
                    jogador1.ultimoMovimento(0, 1)
        #recondicionar personagem
        #direita parte de baixo
        if(rect.x + 30 >= 1151 and rect.y>= 265):
            rect.x -= 2
        #direita parte de cima
        if (rect.x + 30 >= 1021 and rect.y < 265):
            rect.x -=2
        #esquerda parte de baixo
        if rect.x <= 102 and rect.y >= 265:
            rect.x += 2
        #esquerda em cima
        if rect.x <= 229 and rect.y < 265:
            rect.x +=2
        #em cima
        if rect.y < 121 and rect.x > 229 and rect.x < 1021:
            rect.y +=2
        #cima baixo
        if rect.y < 267 and (rect.x <= 229 or rect.x >= 1021):
            rect.y +=2
        #embaixo
        if rect.y + 30 >= 600:
            rect.y = 569
        
        
        colisoes = pygame.sprite.spritecollide(jogador1, areas, False)
        for _ in colisoes:
            print("colidiu")


    ######################################
    ######################################
    ######################################

    #game over ou play again
    elif tela == 4:
        if venceu == 1:
            img_fim = pygame.image.load("imagens/Venceu.png")
        else:
            img_fim = pygame.image.load("imagens/Game_Over.png")
        janela.blit(img_fim, (0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    posicao_seta = 0
                    njogadores = 0
                    njogadores_selecionados = 0
                    inimigos = []
                    tela = 1
                    fonte = pygame.font.Font("freesansbold.ttf", 36)
                    text = fonte.render("Escolha o numero de jogadores", True, (255,255,255))
                else:
                    executando = False    

    pygame.display.flip()

pygame.quit()