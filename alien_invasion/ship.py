import pygame

class Ship:
    ''' 飞船类 '''
    def __init__(self,ai_game):
        ''' 初始化飞船并且设置位置 '''

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载图片和获取图片长宽
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #初始化飞船位置，放在屏幕中间
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        ''' 绘制飞船 '''
        self.screen.blit(self.image,self.rect)