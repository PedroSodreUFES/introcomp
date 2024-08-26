import pygame

import time

import random

import personagens as characters

pygame.init()

# settings janela 
largura = 1280
altura = 720
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Raony Warfare')
icon = pygame.image.load('assets/RAONY.png')    
pygame.display.set_icon(icon)
fps = 60
clock = pygame.time.Clock()
tela = 1

# Fonte Padrao
font = pygame.font.Font(None, 52)

# SOM
pygame.mixer_music.load("audios/sweetdreams.mp3")
pygame.mixer_music.play(-1)
confirmar = pygame.mixer.Sound("audios/confirm.wav")
trocar = pygame.mixer.Sound("audios/mudar.wav")
roundone = pygame.mixer.Sound("audios/mk.mp3")

# imagens primeira tela
imagens_iniciais = ["assets/inicio.png", "assets/inicio1.png" , "assets/inicio2.png", "assets/inicio3.png" , "assets/inicio4.png"]
inicial = 0
mudar_foto = time.time() #lidar com o tempo para mudar a foto


# imagens segunda tela
escolher_personagem = ["assets/choose0.png", "assets/choose1.png", "assets/choose2.png", "assets/choose3.png" , "assets/choose4.png"]
personagem = 0
personagens_escolhidos = 0

# lista de inimigos e aliados
aliados = []
inimigos = []

#imagens gameOver
imagens_fim_de_jogo = ["assets/fimdejogo.png", "assets/fimdejogo1.png"]

#imagens de fundo para quando aliados tiverem jogando:
imagens_aliados = ["assets/sAtacar.png", "assets/sDefender.png", "assets/sInsight.png", "assets/sSkill.png"]

# imagem tela de atacar
atacar = pygame.image.load("assets/ataque.png")

# loop do jogo
exec = True
jogo = True
venceu = True
vez_aliado = 0
vez_inimigo = 0
seta = 0
aliado_ou_inimigo = True
animacao = 0
inimigo_escolhido = 0
jajogou = 0

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
                    personagem = 0
            if evento.type == pygame.QUIT:
                exec = False
        if time.time() - mudar_foto > 0.08:
            mudar_foto = time.time()
            inicial += 1
            if inicial > 4:
                inicial = 0

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

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
                    if personagem >= len(escolher_personagem):
                        personagem = 0
                #selecionou um personagem
                if evento.key == pygame.K_z:
                    # som de confirmar
                    confirmar.play()
                    
                    #escolher o personagem

                    # fireman
                    if escolher_personagem[personagem] == "assets/choose4.png":
                        aliados.append(characters.Fireman(150, 30, 60, 100))
                    # iceman
                    elif escolher_personagem[personagem] == "assets/choose3.png":
                        aliados.append(characters.Iceman(120, 40, 50, 150))
                    # healer
                    elif escolher_personagem[personagem] == "assets/choose2.png":
                        aliados.append(characters.Healer(80, 20, 60, 150))
                    # soldier
                    elif escolher_personagem[personagem] == "assets/choose1.png":
                        aliados.append(characters.Soldier(130, 50, 30, 150))
                    # introcomper
                    elif escolher_personagem[personagem] == "assets/choose0.png":
                        aliados.append(characters.Introcomper(115, 45, 45, 150))


                    escolher_personagem.remove(escolher_personagem[personagem])
                    personagens_escolhidos+=1
                    print(escolher_personagem)
                    print(aliados)
                    print(inimigos)
                    
                    #se a posicao do personagem escolhido era a ultima
                    if personagem > len(escolher_personagem)-1:
                        personagem = len(escolher_personagem) -1

                    # se os 3 personagens foram escolhidos
                    if personagens_escolhidos == 3:
                        # seta os inimigos
                        for x in escolher_personagem:
                            # fireman
                            if x == "assets/choose4.png":
                                inimigos.append(characters.Fireman(180, 30, 60, 150))
                            # iceman
                            elif x == "assets/choose3.png":
                                inimigos.append(characters.Iceman(190, 40, 50, 150))
                            # healer
                            elif x == "assets/choose2.png":
                                inimigos.append(characters.Healer(220, 30, 70, 150))
                            # soldier
                            elif x == "assets/choose1.png":
                                inimigos.append(characters.Soldier(200, 50, 30, 150))
                            # introcomper
                            elif x == "assets/choose0.png":
                                inimigos.append(characters.Introcomper(185, 45, 45, 150))
                            print(escolher_personagem)
                            print(aliados)
                            print(inimigos)
                        #colocar as imagens olhando pro lado certo
                        for aliado in aliados:
                            if aliado.flipparNaEsquerda == 1:
                                aliado.imagem = pygame.transform.flip(aliado.imagem, True, False)
                        for inimigo in inimigos:
                            if inimigo.flipparNaDireita == 1:
                                inimigo.imagem = pygame.transform.flip(inimigo.imagem, True, False)
                        mudar_foto = time.time()
                        time.sleep(0.2)
                        roundone.play()
                        tela = 3

            if evento.type == pygame.QUIT:
                exec = False
    

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

    #gameplay
    elif tela == 3:
        
        # colocar aliados e inimigos como mortos, caso tenham vida < 1
        contAmorto = 0
        for aliado in aliados:
            if aliado.vida < 1:
                aliado.vivo = 0
                aliado.vida = 0
                contAmorto += 1
        if contAmorto == 3:
            jogo = False
            venceu = False
            pygame.mixer_music.load("audios/perdeu.mp3")
            pygame.mixer_music.play(-1)

        contImorto = 0
        for inimigo in inimigos:
            if inimigo.vida < 1:
                inimigo.vivo = 0
                inimigo.vida = 0
                contImorto+=1
        if contImorto == 2:
            jogo = False
            venceu = True
            youwin = pygame.mixer.Sound("audios/youwin.mp3")
            youwin.play()
            pygame.mixer_music.load("audios/musicavitoria.mp3")
            pygame.mixer_music.play(-1)
        
        jajogou = 0
        # vez de um personagem aliado
        if aliado_ou_inimigo and jogo:


            # ver se o personagem atual foi morto
            if aliados[vez_aliado].vivo == 0:
                while True:
                    vez_aliado +=1
                    if vez_aliado >= len(aliados):
                        vez_aliado = 0
                    if aliados[vez_aliado].vivo == 1:
                        break

            # se o personagem tinha defendido um golpe mas nao levou golpe nenhum por 1 round, voltar a defesa ao normal
            if  aliados[vez_aliado].defendi == 1:
                aliados[vez_aliado].defendi = 0
                aliados[vez_aliado].defesa /= 2

            # dar reload na habilidade
            if aliados[vez_aliado].skillAvailable == 0 and aliados[vez_aliado].jadeureload == 0:
                aliados[vez_aliado].reloadSkill +=1
                if aliados[vez_aliado].reloadSkill > 3:
                    aliados[vez_aliado].reloadSkill = 0
                    aliados[vez_aliado].skillAvailable = 1
                aliados[vez_aliado].jadeureload = 1


            # se o aliado não puder jogar por causa do introcomper, skippar ele
            if  aliados[vez_aliado].joga == 0:
                aliados[vez_aliado].joga = 1
                seta = 0
                aliado_ou_inimigo = False
                # fala qual o proximo aliado jogar
                while True:
                    vez_aliado+=1
                    if vez_aliado >= len(aliados):
                        vez_aliado = 0

                    if aliados[vez_aliado].vivo == 1:
                        jajogou = 0
                        break
                continue
                            

            else:

                # printar o fundo
                img_fundo = pygame.image.load(imagens_aliados[seta])
                janela.blit(img_fundo, (0,0))

                #caso o personagem não possa usar a passiva
                if aliados[vez_aliado].skillAvailable == 0:
                    img_fundo = pygame.image.load("assets/noSkill.png")
                    janela.blit(img_fundo, (0,0))

                #printa a mensagem vez do pesonagem
                fonte = pygame.font.Font(None, 52)
                text = fonte.render(f"Vez de {aliados[vez_aliado].nome}", False , (255,255,255))
                janela.blit(text, (500, 40))

                # printar aliados
                x = 320
                y = 30
                a = 1
                for aliado in aliados:
                    if aliado.vivo == 1:
                        if aliado.congelado == 1:
                            congelei = pygame.image.load("assets/congelado.png")
                            janela.blit(congelei, (x, y))
                        if aliado.joga == 0:
                            njoga = pygame.image.load("assets/9.png")
                            janela.blit(njoga, (x,y))

                        janela.blit(aliado.imagem, (x, y))
                        
                        if aliado.granada == 1:
                            granada = pygame.image.load("assets/granada.png")
                            janela.blit(granada, (x, y))
                        aliado.x = x
                        aliado.y = y
                        y+= 120
                        x += a*80
                        a*=-1
                
                # printar inimigos
                x = 800
                y = 80
                for inimigo in inimigos:
                    if inimigo.vivo == 1:
                        if inimigo.congelado == 1:
                            congelei = pygame.image.load("assets/congelado.png")
                            janela.blit(congelei, (x, y))
                        if inimigo.joga == 0:
                            njoga = pygame.image.load("assets/9.png")
                            janela.blit(njoga, (x,y))

                        janela.blit(inimigo.imagem, (x, y))

                        if inimigo.granada == 1:
                            granada = pygame.image.load("assets/granada.png")
                            janela.blit(granada, (x, y))
                        inimigo.x = x
                        inimigo.y = y
                        y += 150

                
                # printa a vida da rapaziada
                fonte = pygame.font.Font(None, 34)
                x = 780
                y = 425 
                for aliado in aliados:
                    if aliado.defendi == 0:
                        text = fonte.render(f"{aliado.nome}: {aliado.vida:.0f}/{aliado.vidaTotal}" , False , (0,151,178))
                    else:
                        text = fonte.render(f"{aliado.nome}: {aliado.vida:.0f}/{aliado.vidaTotal} (DEFENDEU)" , False , (0,151,178))                    
                    janela.blit(text, (x, y))
                    y+=50  
                for inimigo in inimigos:
                    if inimigo.defendi == 0:
                        text = fonte.render(f"{inimigo.nome}: {inimigo.vida:.0f}/{inimigo.vidaTotal}" , False , (0,151,178))
                    else:
                        text = fonte.render(f"{inimigo.nome}: {inimigo.vida:.0f}/{inimigo.vidaTotal} (DEFENDEU)" , False , (0,151,178))               
                    janela.blit(text, (x, y))
                    y+=50 


                # loop dos comandos
                for evento in pygame.event.get():
                    # clicou em fechar aba
                    if evento.type == pygame.QUIT:
                        exec = False

                    # usar teclas    
                    if evento.type == pygame.KEYDOWN:
                        
                        # ir para a esquerda na seleçao do painel
                        if evento.key == pygame.K_LEFT:
                            trocar.play()
                            seta-=1
                            if seta<0 and aliados[vez_aliado].skillAvailable == 1:
                                seta = len(imagens_aliados) -1
                            elif seta < 0 and aliados[vez_aliado].skillAvailable == 0:
                                seta = len(imagens_aliados)-2
                        
                        # ir para a direita na selecao do painel
                        if evento.key == pygame.K_RIGHT:
                            trocar.play()
                            seta+= 1
                            if seta > 2 and aliados[vez_aliado].skillAvailable == 0:
                                seta = 0
                            if seta > 3 and aliados[vez_aliado].skillAvailable == 1:
                                seta = 0
                        
                        # selecionar um golpe
                        if evento.key == pygame.K_z:
                            aliados[vez_aliado].jadeureload = 0
                            confirmar.play()
                            # defender
                            if seta == 1:
                                aliados[vez_aliado].defender()
                                janela.blit(aliados[vez_aliado].defende, (0,0))
                                pygame.display.flip()
                                time.sleep(2)
                                seta = 0
                            
                            # atacar
                            elif seta == 0:

                                # ve quantos inimigos estão vivos
                                cont = 0
                                for inimigo in inimigos:    
                                    if inimigo.vivo == 1:
                                        a = inimigo
                                        cont+=1
                                
                                # só um inimigo vivo
                                if cont == 1:
                                    aliados[vez_aliado].atacar(a)
                                    janela.blit(atacar, (0,0))
                                    janela.blit(aliados[vez_aliado].ataca, (0,0))
                                    janela.blit(a.tomaAtaque, (0,0))
                                    pygame.display.flip()
                                    time.sleep(2)
                                
                                # 2 inimigos vivos
                                else:
                                    x = 780
                                    y = 80
                                    choose = True
                                    seta2 = pygame.image.load("assets/seta2.png")
                                    while choose == True:
                                        
                                        clock.tick(60)

                                        # printa o fundo
                                        img_fundo = pygame.image.load(imagens_aliados[0])
                                        janela.blit(img_fundo, (0,0))

                                        #printa a mensagem atacar
                                        fonte = pygame.font.Font(None, 52)
                                        text = fonte.render("Quem você quer atacar?", False , (255,255,255))
                                        janela.blit(text, (430, 40))

                                        #caso o personagem não possa usar a passiva, printar o menu sem ela
                                        if aliados[vez_aliado].skillAvailable == 0:
                                            img_fundo = pygame.image.load("assets/noSkill.png")
                                            janela.blit(img_fundo, (0,0))

                                        
                                        # printa a setinha para o inimigo desejado
                                        janela.blit(seta2, (x,y))

                                        # printa a vida da rapaziada
                                        fonte = pygame.font.Font(None, 34)
                                        x = 780
                                        y = 425 
                                        for aliado in aliados:
                                            if aliado.defendi == 0:
                                                text = fonte.render(f"{aliado.nome}: {aliado.vida:.0f}/{aliado.vidaTotal}" , False , (0,151,178))
                                            else:
                                                text = fonte.render(f"{aliado.nome}: {aliado.vida:.0f}/{aliado.vidaTotal} (DEFENDEU)" , False , (0,151,178))
                                            janela.blit(text, (x, y))
                                            y+=50  
                                        for inimigo in inimigos:
                                            if inimigo.defendi == 0:
                                                text = fonte.render(f"{inimigo.nome}: {inimigo.vida:.0f}/{inimigo.vidaTotal}" , False , (0,151,178))
                                            else:
                                                text = fonte.render(f"{inimigo.nome}: {inimigo.vida:.0f}/{inimigo.vidaTotal} (DEFENDEU)" , False , (0,151,178))
                                            
                                            janela.blit(text, (x, y))
                                            y+=50 

                                        # printar aliados
                                        x = 320
                                        y = 30
                                        a = 1
                                        for aliado in aliados:
                                            if aliado.vivo == 1:
                                                if aliado.congelado == 1:
                                                    congelei = pygame.image.load("assets/congelado.png")
                                                    janela.blit(congelei, (x, y))
                                                if aliado.joga == 0:
                                                    njoga = pygame.image.load("assets/9.png")
                                                    janela.blit(njoga, (x,y))

                                                janela.blit(aliado.imagem, (x, y))
                            
                                                if aliado.granada == 1:
                                                    granada = pygame.image.load("assets/granada.png")
                                                    janela.blit(granada, (x, y))
                                                y+= 120
                                                x += a*80
                                                a*=-1
                                        
                                        # printar inimigos
                                        x = 800
                                        y = 80
                                        for inimigo in inimigos:
                                            if inimigo.vivo == 1:


                                                janela.blit(inimigo.imagem, (x, y))

                                                if inimigo.granada == 1:
                                                    granada = pygame.image.load("assets/granada.png")
                                                    janela.blit(granada, (x, y))
                                                
                                                y += 150
                                        
                                        # ve os inputs do usuario
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                exec = False
                                                choose = False
                                            if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_LEFT:
                                                    trocar.play()
                                                    seta -= 1
                                                    if seta< 0:
                                                        seta = 1
                                                if event.key == pygame.K_RIGHT:
                                                    trocar.play()
                                                    seta += 1
                                                    if seta > 1:
                                                        seta = 0
                                                if event.key == pygame.K_z:
                                                    confirmar.play()
                                                    aliados[vez_aliado].atacar(inimigos[seta])
                                                    janela.blit(atacar, (0,0))
                                                    janela.blit(aliados[vez_aliado].ataca, (0,0))
                                                    janela.blit(inimigos[seta].tomaAtaque, (0,0))
                                                    pygame.display.flip()
                                                    time.sleep(2)
                                                    choose = False
                                                    seta = 0

                                                    # ve se todos os inimigos morreram já. Se morreram termina o jogo
                                                    contInimigosMortos = 0
                                                    for inimigo in inimigos:
                                                        if inimigo.vida < 1:
                                                            contInimigosMortos+=1
                                                    if contInimigosMortos == 2:
                                                        jogo = False
                                        
                                        if seta == 1:
                                            x = 780
                                            y = 270
                                        if seta == 0:
                                            x = 780
                                            y = 120
                                        
                                        pygame.display.flip()

                            elif seta == 2:
                                print("Raony casa comigo")
                                janela.blit(aliados[vez_aliado].insight, (0,0))
                                pygame.display.flip()
                                time.sleep(5)
                                seta = 2

                            elif seta == 3:
                                janela.blit(aliados[vez_aliado].imagemSkill, (0,0))
                                pygame.display.flip()
                                time.sleep(2)
                                aliados[vez_aliado].passiva(inimigos, aliados, janela, 1)
                                seta = 0
                            jajogou = 1

                            # se o click nao foi em insight
                            if seta != 2:
                                if aliados[vez_aliado].granada == 1:
                                    aliados[vez_aliado].tomaGranada(janela, aliado_ou_inimigo, aliados, inimigos)
                            
                                # fala qual o proximo aliado jogar
                                while jajogou == 1:
                                    vez_aliado+=1
                                    aliado_ou_inimigo = False          
                                    if vez_aliado >= len(aliados):
                                        vez_aliado = 0

                                    if aliados[vez_aliado].vivo == 1:
                                        jajogou = 0
                                        break
            
            
                    
            
                    
                                                                        
                                
#####################################################################################################################
#####################################################################################################################


        # vez de um inimigo
        elif aliado_ou_inimigo == False and jogo:
            if inimigos[vez_inimigo].vivo == 0:
                if vez_inimigo == 0:
                    vez_inimigo = 1
                else:
                    vez_inimigo = 0

            # se o personagem tinha defendido um golpe mas nao levou golpe nenhum por 1 round, voltar a defesa ao normal
            if  inimigos[vez_inimigo].defendi == 1:
                inimigos[vez_inimigo].defendi = 0
                inimigos[vez_inimigo].defesa /= 2

            # dar reload na habilidade
            if inimigos[vez_inimigo].skillAvailable == 0:
                inimigos[vez_inimigo].reloadSkill +=1
                if inimigos[vez_inimigo].reloadSkill > 4:
                    inimigos[vez_inimigo].reloadSkill = 0
                    inimigos[vez_inimigo].skillAvailable = 1

            # se o inimigo não puder jogar por causa do introcomper, skippar ele
            if  inimigos[vez_inimigo].joga == 0:
                    inimigos[vez_inimigo].joga = 1
                    # vez dos aliados
                    aliado_ou_inimigo = True

                    while True:
                        vez_inimigo+=1

                        if vez_inimigo >= len(inimigos):
                            vez_inimigo = 0

                        if inimigos[vez_inimigo].vivo == 1:
                            break
                    
                    continue
            
            else:



                img_fundo = pygame.image.load("assets/vezInimigo.png")
                janela.blit(img_fundo, (0,0))
                
                # printar aliados
                x = 320
                y = 240
                a = 1
                for aliado in aliados:
                    if aliado.vivo == 1:
                        if aliado.congelado == 1:
                            congelei = pygame.image.load("assets/congelado.png")
                            janela.blit(congelei, (x, y))
                        if aliado.joga == 0:
                            njoga = pygame.image.load("assets/9.png")
                            janela.blit(njoga, (x,y))
                        if aliado.granada == 1:
                            granada = pygame.image.load("assets/granada.png")
                            janela.blit(granada, (x, y))
                        janela.blit(aliado.imagem, (x, y))
                        aliado.x = x
                        aliado.y = y
                        y+= 120
                        x += a*80
                        a*=-1
                
                # printar inimigos
                x = 800
                y = 280
                for inimigo in inimigos:
                    if inimigo.vivo == 1:
                        if inimigo.congelado == 1:
                            congelei = pygame.image.load("assets/congelado.png")
                            janela.blit(congelei, (x, y))
                        if inimigo.joga == 0:
                            njoga = pygame.image.load("assets/9.png")
                            janela.blit(njoga, (x,y))
                        janela.blit(inimigo.imagem, (x, y))
                        if inimigo.granada == 1:
                            granada = pygame.image.load("assets/granada.png")
                            janela.blit(granada, (x, y))
                        inimigo.x = x
                        inimigo.y = y
                        y += 150

                # demorar um tempinho para o inimigo jogar
                pygame.display.flip()
                time.sleep(2)


                # jogada do inimigo
                if inimigos[vez_inimigo].skillAvailable == 1:
                    x = random.randint(0, 2)
                

                else:
                    x = random.randint(0,1)
                
                # atacar
                if x == 0:
                    while True:
                        x = random.randint(0,2)
                        if aliados[x].vivo == 1:
                            break
                    inimigos[vez_inimigo].atacar(aliados[x])
                    janela.blit(atacar, (0,0))
                    janela.blit(inimigos[vez_inimigo].ataca, (0,0))
                    janela.blit(aliados[x].tomaAtaque, (0,0))
                    pygame.display.flip()
                    time.sleep(2)
                
                # defender
                elif x == 1:
                    inimigos[vez_inimigo].defender()
                    janela.blit(inimigos[vez_inimigo].defende, (0,0))
                    pygame.display.flip()
                    time.sleep(2)
                
                # passiva
                elif x == 2:
                    janela.blit(inimigos[vez_inimigo].imagemSkill, (0,0))
                    pygame.display.flip()
                    time.sleep(2)
                    inimigos[vez_inimigo].passiva(aliados, inimigos, janela, 0)



            # se tiver uma granada no pé do inimigo
            if inimigos[vez_inimigo].granada == 1:
                inimigos[vez_inimigo].tomaGranada(janela, aliado_ou_inimigo, inimigos, aliados)

            # fala qual o proximo inimigo a jogar
            while True:
                vez_inimigo+=1

                if vez_inimigo >= len(inimigos):
                    vez_inimigo = 0

                if inimigos[vez_inimigo].vivo == 1:
                    break
            


            # vez dos aliados
            aliado_ou_inimigo = True



        # fim do jogo
        if jogo == False:
            tela = 4
            mudar_foto = time.time()
            inicial = 0
            
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

    #gameOver
    elif tela == 4:
        tempo = time.time()
        img_fundo = pygame.image.load(imagens_fim_de_jogo[inicial])
        janela.blit(img_fundo, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:
                    confirmar.play() #som de confirmar
                    while time.time() - tempo < 0.5:
                        exec = False
            if evento.type == pygame.QUIT:
                exec = False
        if time.time() - mudar_foto > 0.6:
            mudar_foto = time.time()
            inicial += 1
            if inicial > 1:
                inicial = 0

    pygame.display.flip()

pygame.quit()      