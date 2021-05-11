import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    ''' 游戏主类，用于管理整个游戏 '''

    def __init__(self):
        ''' 初始化游戏并创建资源 '''
        pygame.init()

        #创建设置类对象
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        #创建飞船对象
        self.ship = Ship(self)
        
    def run_game(self):
        ''' 游戏循环 '''
        while True:
            #监测输入事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #填充屏幕颜色
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()#调用飞船绘制方法绘制飞船
            #绘制屏幕
            pygame.display.flip()

if __name__ == '__main__':
    ''' 利用主类创建实例并运行 '''
    ai = AlienInvasion()
    ai.run_game()