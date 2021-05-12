import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 管理外星人的类 """
    def __init__(self,ai_game):
        ''' 初始化外星人属性 '''
        super().__init__()
        self.screen = ai_game.screen
        
        #加载外星人图片并获取图片矩形属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #初始化外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #获取外星人浮点位置X
        self.x = float(self.rect.x)