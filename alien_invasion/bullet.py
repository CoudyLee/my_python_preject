import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' 子弹类 '''
    def __init__(self,ai_game):
        ''' 初始化子弹对象 '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #设置子弹初始位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #设置浮点小数的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        ''' 更新子弹状态 '''
        #根据子弹速度更新子弹浮点位置
        self.y -= self.settings.bullet_speed
        #根据浮点位置更新子弹矩形屏幕位置
        self.rect.y = self.y

    def draw_bullet(self):
        ''' 在屏幕上绘制子弹 '''
        pygame.draw.rect(self.screen,self.color,self.rect)

