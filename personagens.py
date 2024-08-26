import pygame

import time 

class Geral(pygame.sprite.Sprite):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__()
        self.vida = vida
        self.vidaTotal = vida
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.congelado = 0
        self.pegandofogo = 0
        self.joga = 1 # diz se o personagem pode jogar nessa rodada
        self.skillAvailable = 1 # diz se o personagem pode usar sua habilidade
        self.granada = 0
        self.flipparNaEsquerda = 0
        self.flipparNaDireita = 0
        self.healado = 0
        self.defendi = 0
        self.vivo = 1
        self.reloadSkill = 0
        self.x = 0
        self.y = 0
        self.jadeureload = 0

    def atacar(self, inimigo):
        inimigo.vida -= round(self.ataque * (50/(50 + inimigo.defesa)), 0)
        if inimigo.defendi == 1:
            inimigo.defendi = 0
            inimigo.defesa /= 2
        if self.congelado == 1:
            self.congelado = 0
            self.ataque *=3
        if inimigo.vida < 1:
            inimigo.vivo = 0

    def defender(self):
        self.defesa = self.defesa * 2
        self.defendi = 1
    
    def tomaGranada(self, janela, aliado_inimigo, aliados, inimigos):
        granada = pygame.image.load("assets/explosao.png")
        explosao = pygame.mixer.Sound("audios/explosao.wav")
        if aliado_inimigo:
            imagem_fundo = pygame.image.load("assets/sSkill.png")
        else:
            imagem_fundo = pygame.image.load("assets/vezInimigo.png")
        janela.blit(imagem_fundo, (0,0))
        for aliado in aliados:
            if aliado.vivo == 1:
                janela.blit(aliado.imagem, (aliado.x, aliado.y))
        for inimigo in inimigos:
            if inimigo.vivo == 1:
                janela.blit(inimigo.imagem, (inimigo.x, inimigo.y))
        
        janela.blit(granada, (self.x, self.y))
        explosao.play()
        pygame.display.flip()
        time.sleep(2)
        if self.defendi == 1:
            self.vida -= 5
            self.defendi = 0
        else:
            self.vida -= 30
        self.granada = 0


class Introcomper(Geral):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)
        self.flipparNaDireita = 1
        self.imagem = pygame.image.load("assets/introcomper.png")
        self.imagemSkill = pygame.image.load("assets/skillintrocomper.png")
        self.insight = pygame.image.load("assets/hintrocomper.png")
        self.nome = "Introcomper"
        self.tomaAtaque = pygame.image.load("assets/tintrocomper.png")
        self.ataca = pygame.image.load("assets/aintrocomper.png")
        self.defende = pygame.image.load("assets/dintrocomper.png")

    def passiva(self, enemiesList, alliesList, janela, inimigo_ou_aliado):
        for enemy in enemiesList:
            enemy.joga = 0
        self.skillAvailable = 0

        audio =  pygame.mixer.Sound("audios/introcomper.wav")
        if inimigo_ou_aliado == 1:
            imagem_fundo = pygame.image.load("assets/sInsight.png")
        else:
            imagem_fundo = pygame.image.load("assets/vezInimigo.png")
        janela.blit(imagem_fundo, (0,0))

        for aliado in alliesList:
            if aliado.vivo == 1:
                janela.blit(aliado.imagem, (aliado.x, aliado.y))

        for inimigo in enemiesList:
            bloqueado = pygame.image.load("assets/9.png")
            if inimigo.vivo == 1:
                janela.blit(bloqueado, (inimigo.x, inimigo.y))
                janela.blit(inimigo.imagem, (inimigo.x, inimigo.y))
                pygame.display.flip()
                audio.play()
                time.sleep(1)

class Soldier(Geral):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)
        self.flipparNaDireita = 1
        self.imagem = pygame.image.load("assets/soldier.png")
        self.imagemSkill = pygame.image.load("assets/skillsoldier.png")
        self.nome = "Soldier"
        self.insight = pygame.image.load("assets/hsoldier.png")
        self.tomaAtaque = pygame.image.load("assets/tsoldier.png")
        self.ataca = pygame.image.load("assets/asoldier.png")
        self.defende = pygame.image.load("assets/dsoldier.png")

    def passiva(self, enemiesList, alliesList, janela, inimigo_ou_aliado):
        for enemy in enemiesList:
            enemy.granada = 1
        self.skillAvailable = 0

    

class Healer(Geral):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)
        self.flipparNaEsquerda = 1
        self.imagem = pygame.image.load("assets/healer.png")
        self.imagemSkill = pygame.image.load("assets/skillhealer.png")
        self.nome = "Healer"
        self.insight = pygame.image.load("assets/hhealer.png")
        self.tomaAtaque = pygame.image.load("assets/thealer.png")
        self.ataca = pygame.image.load("assets/ahealer.png")
        self.defende = pygame.image.load("assets/dhealer.png")

    def passiva(self, enemiesList, alliesList, janela, inimigo_ou_aliado):
        for  ally in alliesList:
            ally.vida += 30
        self.skillAvailable = 0

        audio =  pygame.mixer.Sound("audios/curar.wav")
        if inimigo_ou_aliado == 1:
            imagem_fundo = pygame.image.load("assets/sInsight.png")
        else:
            imagem_fundo = pygame.image.load("assets/vezInimigo.png")
        janela.blit(imagem_fundo, (0,0))

        for inimigo in enemiesList:
            if inimigo.vivo == 1:
                janela.blit(inimigo.imagem, (inimigo.x, inimigo.y))

        cura = pygame.image.load("assets/10.png")
        for aliado in alliesList:
            if aliado.vivo == 1:
                janela.blit(cura, (aliado.x, aliado.y))
                janela.blit(aliado.imagem, (aliado.x, aliado.y))
                audio.play()
                pygame.display.flip()
                time.sleep(1)
        
        
                


class Fireman(Geral):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)
        self.flipparNaEsquerda = 1
        self.imagem = pygame.image.load("assets/fireman.png")
        self.imagemSkill = pygame.image.load("assets/skillfireman.png")
        self.nome = "Fireman"
        self.insight = pygame.image.load("assets/hfireman.png")
        self.tomaAtaque = pygame.image.load("assets/tfireman.png")
        self.ataca = pygame.image.load("assets/afireman.png")
        self.defende = pygame.image.load("assets/dfireman.png")

    def passiva(self, enemiesList, alliesList, janela, inimigo_ou_aliado):
        audio =  pygame.mixer.Sound("audios/fogo.ogg")
        if inimigo_ou_aliado == 1:
            imagem_fundo = pygame.image.load("assets/sInsight.png")
        else:
            imagem_fundo = pygame.image.load("assets/vezInimigo.png")
        janela.blit(imagem_fundo, (0,0))
        for enemy in enemiesList:
            enemy.vida -= 30
        self.skillAvailable = 0

        for aliado in alliesList:
            if aliado.vivo == 1:
                janela.blit(aliado.imagem, (aliado.x, aliado.y))

        for inimigo in enemiesList:
            fogo = pygame.image.load("assets/fogo.png")
            if inimigo.vivo == 1:
                janela.blit(fogo, (inimigo.x, inimigo.y))
                janela.blit(inimigo.imagem, (inimigo.x, inimigo.y))
                pygame.display.flip()
                audio.play()
                time.sleep(2)

class Iceman(Geral):
    def __init__(self, vida, ataque, defesa, velocidade):
        super().__init__(vida, ataque, defesa, velocidade)
        self.flipparNaEsquerda = 1
        self.imagem = pygame.image.load("assets/iceman.png")
        self.imagemSkill = pygame.image.load("assets/skilliceman.png")
        self.nome = "Iceman"
        self.insight = pygame.image.load("assets/hiceman.png")
        self.tomaAtaque = pygame.image.load("assets/ticeman.png")
        self.ataca = pygame.image.load("assets/aiceman.png")
        self.defende = pygame.image.load("assets/diceman.png")

    def passiva(self, enemiesList, alliesList, janela, inimigo_ou_aliado):
        for enemy in enemiesList:
            enemy.congelado = 1
            enemy.ataque = enemy.ataque / 3
        self.skillAvailable = 0

        audio =  pygame.mixer.Sound("audios/gelo.wav")
        if inimigo_ou_aliado == 1:
            imagem_fundo = pygame.image.load("assets/sInsight.png")
        else:
            imagem_fundo = pygame.image.load("assets/vezInimigo.png")
        janela.blit(imagem_fundo, (0,0))

        for aliado in alliesList:
            if aliado.vivo == 1:
                janela.blit(aliado.imagem, (aliado.x, aliado.y))

        audio.play()
        for inimigo in enemiesList:
            gelei = pygame.image.load("assets/congelado.png")
            if inimigo.vivo == 1:
                janela.blit(gelei, (inimigo.x, inimigo.y))
                janela.blit(inimigo.imagem, (inimigo.x, inimigo.y))
                pygame.display.flip()
                time.sleep(1)
        