import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_YELLOW, C_ORANGE


class Rules:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            # Draw background
            self.window.blit(source=self.surf, dest=self.rect)

            # Title
            self.rules_text(40, 'RULES', C_ORANGE, (WIN_WIDTH / 2, 80))

            # Rule lines
            self.rules_text(22, "Don't touch the walls!", C_YELLOW, (WIN_WIDTH / 2, 160))
            self.rules_text(18, 'Use arrow keys to move the player.', C_WHITE, (WIN_WIDTH / 2, 195))
            self.rules_text(18, 'Reach the exit to advance to the next level.', C_WHITE, (WIN_WIDTH / 2, 220))

            # Back button hint
            self.rules_text(16, '[ESC]  Back to Menu', C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT - 20))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                        return  # back to menu

    def rules_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)