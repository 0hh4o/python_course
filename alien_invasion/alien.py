import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """显示一个外星人在屏幕上"""

    def __init__(self, ai_settings, screen):
        """初始化外星人，设置初始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，定义它的外接矩形
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人在屏幕边缘返回真"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """移动外星人左右移动"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """显示外星人图像在它的位置上"""
        self.screen.blit(self.image, self.rect)
