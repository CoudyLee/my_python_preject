import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 管理外星人的类 """
    def __init__(self,ai_game):
        ''' 初始化外星人属性 '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #加载外星人图片并获取图片矩形属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #初始化外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #获取外星人浮点位置X
        self.x = float(self.rect.x)

    def check_edges(self):
        ''' 检测外星人是否大于或小于画布两边 '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        ''' 更新外星人位置 '''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x