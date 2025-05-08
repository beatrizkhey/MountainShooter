#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')  # Carrega a imagem para a variável surf desta instância
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  # Desenha um retângulo e o inicia nas coordenadas fornecidas da surf

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')  # Carrega a música
        pygame.mixer_music.play(-1)  # Toca a música, -1 para tocar sem parar
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem surf (origem) no retângulo (destino)
            self.menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), (200 + 25 * i)))

            pygame.display.flip()  # Atualiza a imagem na tela

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)  # Indica a fonte que será utilizada
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Cria a imagem
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Desenha o retângulo
        self.window.blit(source=text_surf, dest=text_rect)  # "Desenha" o texto no retângulo de texto
