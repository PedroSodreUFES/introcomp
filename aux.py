import pygame

def desenha_os_cards(tela):
    #200 = 10 do atributo
    pygame.draw.rect(tela, (253, 174, 151), pygame.Rect(20, 150, 300, 400))
    pygame.draw.rect(tela, (253, 174, 151), pygame.Rect(330, 150, 300, 400))
    pygame.draw.rect(tela, (253, 174, 151), pygame.Rect(640, 150, 300, 400))
    pygame.draw.rect(tela, (253, 174, 151), pygame.Rect(950, 150, 300, 400))
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    # card Assasssino
    text = fonte.render("Assassino", True, (0,0,0))
    tela.blit(text, (115, 180))
    fonte = pygame.font.Font("freesansbold.ttf", 16)
    #
    text = fonte.render("Vida:", True, (0,0,0))
    tela.blit(text, (30, 420))
    pygame.draw.rect(tela, (186, 0, 0), pygame.Rect(100, 424, 160, 10))
    #
    text = fonte.render("Rapidez:", True, (0,0,0))
    tela.blit(text, (30, 440))
    pygame.draw.rect(tela, (0, 0, 186), pygame.Rect(100, 444, 200, 10))
    #
    text = fonte.render("Força:", True, (0,0,0))
    tela.blit(text, (30, 460))
    pygame.draw.rect(tela, (0, 186, 0), pygame.Rect(100, 464, 133, 10))
    img_fundo = pygame.image.load("imagens/assassino.png")
    tela.blit(img_fundo, (60, 210))
    
    ##################################################################

    fonte = pygame.font.Font("freesansbold.ttf", 20)
    # card Tanque
    text = fonte.render("Tanque", True, (0,0,0))
    tela.blit(text, (440,180))
    fonte = pygame.font.Font("freesansbold.ttf", 16)
    #
    text = fonte.render("Vida:", True, (0,0,0))
    tela.blit(text, (340, 420))
    pygame.draw.rect(tela, (186, 0, 0), pygame.Rect(410, 424, 200, 10))
    #
    text = fonte.render("Rapidez:", True, (0,0,0))
    tela.blit(text, (340, 440))
    pygame.draw.rect(tela, (0, 0, 186), pygame.Rect(410, 444, 100, 10))
    #
    text = fonte.render("Força:", True, (0,0,0))
    tela.blit(text, (340, 460))
    pygame.draw.rect(tela, (0, 186, 0), pygame.Rect(410, 464, 200, 10))
    img_fundo = pygame.image.load("imagens/tanque.png")
    tela.blit(img_fundo, (375, 210))
    


    ##################################################################
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    # Card atirador
    text = fonte.render("Atirador", True, (0,0,0))
    tela.blit(text, (745,180))
    fonte = pygame.font.Font("freesansbold.ttf", 16)
    #
    text = fonte.render("Vida:", True, (0,0,0))
    tela.blit(text, (650, 420))
    pygame.draw.rect(tela, (186, 0, 0), pygame.Rect(720, 424, 120, 10))
    #
    text = fonte.render("Rapidez:", True, (0,0,0))
    tela.blit(text, (650, 440))
    pygame.draw.rect(tela, (0, 0, 186), pygame.Rect(720, 444, 160, 10))
    #
    text = fonte.render("Força:", True, (0,0,0))
    tela.blit(text, (650, 460))
    pygame.draw.rect(tela, (0, 186, 0), pygame.Rect(720, 464, 200, 10))
    img_fundo = pygame.image.load("imagens/atirador.png")
    tela.blit(img_fundo, (680, 210))

    ##################################################################
    fonte = pygame.font.Font("freesansbold.ttf", 20)
    # card Mago
    text = fonte.render("Mago", True, (0,0,0))
    tela.blit(text, (1070,180))
    fonte = pygame.font.Font("freesansbold.ttf", 16)
    #
    text = fonte.render("Vida:", True, (0,0,0))
    tela.blit(text, (960, 420))
    pygame.draw.rect(tela, (186, 0, 0), pygame.Rect(1030, 424, 200, 10))
    #
    text = fonte.render("Rapidez:", True, (0,0,0))
    tela.blit(text, (960, 440))
    pygame.draw.rect(tela, (0, 0, 186), pygame.Rect(1030, 444, 160, 10))
    #
    text = fonte.render("Força:", True, (0,0,0))
    tela.blit(text, (960, 460))
    pygame.draw.rect(tela, (0, 186, 0), pygame.Rect(1030, 464, 133, 10))
    img_fundo = pygame.image.load("imagens/mago.png")
    tela.blit(img_fundo, (990, 210))
    
    




