import pygame

import time

import random

pygame.init()

# settings janela 
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Raony, o Jogo!')
icon = pygame.image.load('assets/RAONY.png')    
pygame.display.set_icon(icon)
fps = 60
clock = pygame.time.Clock()
tela = 1

# Fonte Padrao
font = pygame.font.Font(None, 52)

# SOM
pygame.mixer_music.load("audios/Peaches.m4a")
pygame.mixer_music.play(-1)
confirmar = pygame.mixer.Sound("audios/confirm.wav")
trocar = pygame.mixer.Sound("audios/mudar.wav")

# imagens primeira tela
imagens_iniciais = ["assets/inicio.png", "assets/inicio1.png" , "assets/inicio2.png", "assets/inicio3.png" , "assets/inicio4.png"]
inicial = 0
mudar_foto = time.time() #lidar com o tempo para mudar a foto


# imagens segunda tela
escolher_personagem = ["assets/choose0.png", "assets/choose1.png", "assets/choose2.png", "assets/choose3.png" , "assets/choose4.png"]
personagem = 0
personagens_escolhidos = 0
aliados = []
inimigos = []

# loop do jogo
exec = True
while exec == True:
    
    clock.tick(60)

    #inicio
    if tela == 1:
        img_fundo = pygame.image.load(imagens_iniciais[inicial])
        janela.blit(img_fundo, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    confirmar.play() #som de confirmar
                    tela = 2
            if evento.type == pygame.QUIT:
                exec = False
        if time.time() - mudar_foto > 0.08:
            mudar_foto = time.time()
            inicial += 1
            if inicial > 4:
                inicial = 0
    
    #choose character
    elif tela == 2:
        img_fundo = pygame.image.load(escolher_personagem[personagem])
        janela.blit(img_fundo, (0, 0))
        font = pygame.font.Font(None, 52)
        text = font.render(f"Escolha mais {3-personagens_escolhidos} personagens", True, (255,255,255))
        janela.blit(text, (400, 30))
        font = pygame.font.Font(None,36)
        text = font.render("Use 'z' para confirmar o personagem e <- ou -> para alterar o personagem", True, (255, 255, 255))
        janela.blit(text, (200, 80))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                #setinha para esquerda
                if evento.key == pygame.K_LEFT:
                    trocar.play() # som para mudar de personagem
                    personagem -= 1
                    if personagem < 0:
                        personagem = len(escolher_personagem) - 1
                #setinha para a direita                
                if evento.key == pygame.K_RIGHT:
                    trocar.play() # som para mudar de personagem
                    personagem += 1
                    if personagem == len(escolher_personagem):
                        personagem = 0
                #selecionou um personagem
                if evento.key == pygame.K_z:
                    confirmar.play() # som de confirmar
                    escolher_personagem.pop(personagem)
                    personagens_escolhidos+=1
                    #se a posicao do personagem escolhido era a ultima
                    if personagem >= len(escolher_personagem):
                        personagem = len(escolher_personagem) - 1
                    if personagens_escolhidos == 3:
                        tela = 3
                        mudar_foto = time.time()
                        while time.time() - mudar_foto < 0.2:
                            tela = 3 
            if evento.type == pygame.QUIT:
                exec = False
    

    #gameplay
    elif tela == 3:
        exec = False


    pygame.display.flip()


pygame.quit()