import pygame


class Stats:
    """
        forca
        vida
        vel
    """
    def __init__(self, forca: int, vida: int, velocidade: int):
        self.forca = forca
        self.vida = vida
        self.velocidade = velocidade

    # funcoes de get #
    def get_forca(self) -> int:
        return self.forca

    def get_vida(self) -> int:
        return self.vida

    def get_velocidade(self) -> int:
        return self.velocidade

    # funcoes de set #
    def set_forca(self, new_forca) -> None:
        self.forca = new_forca

    def set_vida(self, new_vida) -> None:
        self.vida = new_vida

    def set_velocidade(self, new_velocidade) -> None:
        self.velocidade = new_velocidade

    # funcoes logicas #
    def esta_vivo(self) -> bool:
        if self.vida > 0:
            return True
        else:
            return False

    def recebe_dano(self, ataque: int) -> None:
        self.vida -= ataque
        if self.vida < 0:
            self.vida = 0


class Mago(Stats):
    """
        fisico
        projetil
        aoe
        passiva
        utility
    """
    def __init__(self):
        super().__init__(10, 20, 30)

    def ataque_fisico(self):
        return

    def ataque_projetil(self):
        return

    def ataque_em_area(self):
        return

    def passiva(self):
        return

    def utility(self):
        return

