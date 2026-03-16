import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import (WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_YELLOW, C_RED,
                        LEVEL_BG, LEVEL_EXITS, PLAYER_START, LEVEL_SONG)
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str):
        self.window = window
        self.name = name
        self.surf = pygame.image.load(f'./asset/{LEVEL_BG[name]}.png').convert()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.player = Player(position=PLAYER_START[name])
        self.exit_rects: list[Rect] = LEVEL_EXITS[name]

    def run(self) -> bool:
        """
        Returns True  → player reached exit
        Returns False → player died or pressed ESC
        """
        pygame.mixer.music.load(LEVEL_SONG[self.name])
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # --- Draw ---
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.player.surf, dest=self.player.rect)

            # HUD
            self.level_text(14, f'{self.name}', C_WHITE, (10, 5))
            self.level_text(12, 'Reach the exit!', C_YELLOW, (WIN_WIDTH - 10, 5), align='right')
            self.level_text(12, '[ESC] Menu', C_WHITE, (10, WIN_HEIGHT - 15))

            pygame.display.flip()

            # --- Events ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        return False

            # --- Move ---
            self.player.move(self.surf)

            # --- Death check ---
            if not self.player.alive:
                pygame.mixer.music.stop()
                self.__show_game_over()
                return False

            # --- Exit check: any rect in the list triggers advance ---
            for exit_rect in self.exit_rects:
                if exit_rect.colliderect(self.player.rect):
                    pygame.mixer.music.stop()
                    return True

    def __show_game_over(self):
        font_big = pygame.font.SysFont('Lucida Sans Typewriter', 52)
        font_sub = pygame.font.SysFont('Lucida Sans Typewriter', 20)
        start_ticks = pygame.time.get_ticks()

        while True:
            if pygame.time.get_ticks() - start_ticks > 2500:
                return

            self.window.blit(source=self.surf, dest=self.rect)
            go_surf  = font_big.render('GAME OVER', True, C_RED)
            sub_surf = font_sub.render("Don't touch the walls!", True, C_WHITE)
            self.window.blit(go_surf,  go_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30)))
            self.window.blit(sub_surf, sub_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30)))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def level_text(self, text_size: int, text: str, text_color: tuple,
                   text_pos: tuple, align: str = 'left'):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if align == 'right':
            text_rect: Rect = text_surf.get_rect(right=text_pos[0], top=text_pos[1])
        else:
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)