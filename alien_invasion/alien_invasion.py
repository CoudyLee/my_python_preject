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

        #窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        #全屏
#        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #创建飞船对象
        self.ship = Ship(self)
        
    def run_game(self):
        ''' 游戏循环 '''
        while True:
            #调用输入事件方法
            self._check_events()
            #更新飞船位置
            self.ship.update()
            #调用刷新画面方法
            self._update_screen()

    def _check_events(self):
        ''' 监测输入事件 '''
        for event in pygame.event.get():
            #监测到点击窗口X按钮后关闭窗口
            if event.type == pygame.QUIT:
                sys.exit()

            #监测键盘事件
            elif event.type == pygame.KEYDOWN:  #监测按下
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:    #监测松开
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        ''' 监测按下事件 '''
        if event.key == pygame.K_RIGHT:
            #开启飞船对象右移状态
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #开启左移状态
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #按q关闭程序
            sys.exit()

    def _check_keyup_events(self,event):
        ''' 监测松开事件 '''
        if event.key == pygame.K_RIGHT:
            #关闭右移状态
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
                    #关闭左移状态
            self.ship.moving_left = False


    def _update_screen(self):
        ''' 负责画面刷新的方法 '''
        #填充屏幕颜色
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()#调用飞船绘制方法绘制飞船

        #绘制屏幕
        pygame.display.flip()

if __name__ == '__main__':
    ''' 利用主类创建实例并运行 '''
    ai = AlienInvasion()
    ai.run_game()