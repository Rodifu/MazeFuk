import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, LEVEL_ORDER
from code.Level import Level
from code.Menu import Menu
from code.Rules import Rules


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('MazeFuk')

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:       # START GAME
                self.__run_levels()

            elif menu_return == MENU_OPTION[1]:     # RULES
                rules = Rules(self.window)
                rules.run()

            elif menu_return == MENU_OPTION[2]:     # EXIT
                pygame.quit()
                sys.exit()

    def __run_levels(self):
        """Run all levels in order. Stop if player quits mid-level."""
        for level_name in LEVEL_ORDER:
            level = Level(self.window, level_name)
            result = level.run()
            if not result:
                # Player pressed ESC — return to main menu
                return
        # All levels completed — back to menu (could show win screen here)
        self.__show_win_screen()

    def __show_win_screen(self):
        """Simple 'You Win' screen shown after completing all levels."""
        font = pygame.font.SysFont('Lucida Sans Typewriter', 48)
        sub  = pygame.font.SysFont('Lucida Sans Typewriter', 20)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            self.window.fill((0, 0, 0))
            win_surf = font.render('YOU WIN!', True, (255, 220, 0))
            sub_surf = sub.render('Press ENTER to return to menu', True, (255, 255, 255))
            self.window.blit(win_surf, win_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30)))
            self.window.blit(sub_surf, sub_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30)))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        return