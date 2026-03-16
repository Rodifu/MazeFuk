import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION, MENU_SONG, C_WALL


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self) -> str:
        pygame.mixer.music.load(MENU_SONG)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(60, 'MazeFuk', C_WALL, (WIN_WIDTH / 2, 100))

            for i in range(len(MENU_OPTION)):
                color = C_YELLOW if i == menu_option else C_WHITE
                self.menu_text(22, MENU_OPTION[i], color, (WIN_WIDTH / 2, 260 + 38 * i))

            self.menu_text(13, 'UP/DOWN to navigate   ENTER to select', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT - 15))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)