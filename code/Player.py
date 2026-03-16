import pygame
from pygame import Surface

from code.Const import (PLAYER_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN,
                        PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT,
                        WIN_WIDTH, WIN_HEIGHT, C_WALL, COLLISION_MARGIN)


class Player:
    def __init__(self, position: tuple):
        self.surf = pygame.image.load('./asset/player.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.alive = True

    def move(self, level_surf: Surface):
        """Move player; if wall is touched, player dies."""
        pressed = pygame.key.get_pressed()

        if pressed[PLAYER_KEY_UP]:
            self.rect.y -= PLAYER_SPEED
        if pressed[PLAYER_KEY_DOWN]:
            self.rect.y += PLAYER_SPEED
        if pressed[PLAYER_KEY_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if pressed[PLAYER_KEY_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Keep inside window bounds
        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

        # Wall touch = death
        if self.__hits_wall(level_surf):
            self.alive = False

    def __hits_wall(self, level_surf: Surface) -> bool:
        """
        Sample 8 points around the player edges.
        Returns True if any point matches C_WALL color.
        """
        m = COLLISION_MARGIN
        check_points = [
            (self.rect.left  + m, self.rect.top     + m),  # top-left
            (self.rect.right - m, self.rect.top     + m),  # top-right
            (self.rect.left  + m, self.rect.bottom  - m),  # bottom-left
            (self.rect.right - m, self.rect.bottom  - m),  # bottom-right
            (self.rect.centerx,   self.rect.top     + m),  # top-center
            (self.rect.centerx,   self.rect.bottom  - m),  # bottom-center
            (self.rect.left  + m, self.rect.centery),      # left-center
            (self.rect.right - m, self.rect.centery),      # right-center
        ]

        surf_w = level_surf.get_width()
        surf_h = level_surf.get_height()

        for (px, py) in check_points:
            px = max(0, min(px, surf_w - 1))
            py = max(0, min(py, surf_h - 1))
            color = level_surf.get_at((px, py))[:3]
            if color == C_WALL:
                return True
        return False