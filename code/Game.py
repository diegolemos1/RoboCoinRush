#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.screen)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()  # Close Screen
                quit()  # end pygame
            else:
                pass
