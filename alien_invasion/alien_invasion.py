import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        self.ship = Ship(self)                  #创建飞船对象
        self.bullets = pygame.sprite.Group()    #创建子弹列表
        self.aliens = pygame.sprite.Group()     #创建外星人列表

        self._create_fleet()                    #初始化一群外星人

    def run_game(self):
        ''' 游戏循环 '''
        while True:
            #调用输入事件方法
            self._check_events()
            #更新飞船位置
            self.ship.update()
            #更新子弹状态
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
            #按空格创建子弹对象
            self._fire_bullet()

    def _check_keyup_events(self,event):
        ''' 监测松开事件 '''
        if event.key == pygame.K_RIGHT:
            #关闭右移状态
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            #关闭左移状态
            self.ship.moving_left = False

    def _fire_bullet(self):
        ''' 创建子弹，并加入子弹列表 '''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        ''' 负责画面刷新的方法 '''
        #填充屏幕颜色
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()#调用飞船绘制方法绘制飞船

        #循环子弹列表，并调用各个实例的渲染方法
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #绘制外星人列表
        self.aliens.draw(self.screen)

        #绘制屏幕
        pygame.display.flip()

    def _update_bullets(self):
        ''' 更新子弹状态 '''
        #更新子弹列表各子弹位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _create_fleet(self):
        ''' 创建一群外星人 '''
        #创建一个外星人实例并放入列表
        alien = Alien(self)
        self.aliens.add(alien)

if __name__ == '__main__':
    ''' 利用主类创建实例并运行 '''
    ai = AlienInvasion()
    ai.run_game()