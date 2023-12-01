import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理从飞船上发射子弹的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船的当前位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建子弹的外接矩形，设置它的位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 将子弹位置存储为一个值
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """让子弹向上移动"""
        # 更新子弹位置
        self.y -= self.speed_factor
        # 更新子弹的外接矩形
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上显示子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
