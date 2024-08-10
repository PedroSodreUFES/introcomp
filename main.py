import pygame

import random

import aux

from buttons import Buttons

pygame.init()

#settings janela 
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))
fps = 60
clock = pygame.time.Clock()

#telas de fundo
img_fundo = pygame.image.load("imagens/pagina_de_jogar.png")

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

#carregar seta
seta = pygame.image.load("imagens/seta.png")
seta = pygame.transform.scale_by(seta, 0.5)
seta2 = pygame.image.load("imagens/seta_para_cima.png")

#jogadores
jogador1 = {}
jogador2 = {}

#imagem fundo
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
                    njogadores_selecionados+=1
                    if(njogadores == njogadores_selecionados):
                        tela = 3

    #porradaria
    elif tela == 3:
        janela.blit(img_mapa, (0,0))
        tela = 4
    
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
                    tela = 1
                    fonte = pygame.font.Font("freesansbold.ttf", 36)
                    text = fonte.render("Escolha o numero de jogadores", True, (255,255,255))
                else:
                    executando = False    

    pygame.display.flip()

pygame.quit()