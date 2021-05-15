import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    ''' 飞船类 '''
    def __init__(self,ai_game):
        ''' 初始化飞船并且设置位置 '''
        super().__init__()
        self.screen = ai_game.screen                    #获取朱磊屏幕对象
        self.settings = ai_game.settings                #获取主类设置对象的属性
        self.screen_rect = ai_game.screen.get_rect()    #获取主类屏幕大小

        #加载图片和获取图片长宽
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #初始化飞船位置，放在屏幕中间
        self.rect.midbottom = self.screen_rect.midbottom

        #飞船X值转化为float
        self.x = float(self.rect.x)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        ''' 飞船状态更新 '''

        #改变飞船X的值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #根据floatX的值，调整飞船屏幕位置，飞船rect对象只能接受整数
        self.rect.x = self.x

    def blitme(self):
        ''' 绘制飞船 '''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        ''' 重置飞船 '''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)