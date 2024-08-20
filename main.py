import pygame

pygame.init()

#settings janela 
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Raony irado!!!!!!!!!!!!!!!!!!')
icon = pygame.image.load('assets/RAONY.png')    
pygame.display.set_icon(icon)
fps = 60
clock = pygame.time.Clock()
tela = 1
exec = True
pygame.mixer_music.load("audios/Ayrton-Senna-Tema-da-vitoria_-.mp3")
pygame.mixer_music.play(1)

#imagens
img_fundo = pygame.image.load("assets/intro.png")
while exec == True:
    
    clock.tick(60)

    if tela == 1:
        janela.blit(img_fundo, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    tela = 2
                    exec = False

    pygame.display.flip()
pygame.quit()