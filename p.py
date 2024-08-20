import pygame

# Inicializar o Pygame
pygame.init()

# Configuração da janela do jogo
largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pega Pega")

# Cores
cor_fundo = (0, 0, 0)        # Preto
cor_jogador = (255, 255, 255)  # Branco

# Criação da classe do sprite do jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tamanho = (50, 50)
        self.rect = pygame.Rect((largura // 2 - self.tamanho[0] // 2, altura - self.tamanho[1]), self.tamanho)
        self.velocidade = 0

    def desenhar_jogador(self, tela):
        pygame.draw.rect(tela, cor_jogador, self.rect)

    def atualizar(self):
        self.rect.x += self.velocidade

# Criar o sprite do jogador
jogador = Jogador()

# Loop do jogo
executando = True
clock = pygame.time.Clock()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jogador.velocidade = -5
            elif evento.key == pygame.K_RIGHT:
                jogador.velocidade = 5
        elif evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jogador.velocidade = 0

    # Preencher a janela com a cor de fundo
    janela.fill(cor_fundo)

    # Atualizar o jogador
    jogador.atualizar()

    # Desenhar o jogador
    jogador.desenhar_jogador(janela)

    # Atualizar a exibição
    pygame.display.flip()

    # Definir a taxa de quadros
    clock.tick(60)

# Encerrar o jogo
pygame.quit()


