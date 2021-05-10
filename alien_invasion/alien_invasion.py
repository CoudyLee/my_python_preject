import sys
import pygame

class AlienInvasion:
    ''' 游戏主类，用于管理整个游戏 '''

    def __init__(self):
        ''' 初始化游戏并创建资源 '''
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        ''' 游戏循环 '''
        while True:
            #监测输入事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #绘制屏幕
            pygame.display.flip()

if __name__ == '__main__':
    ''' 利用主类创建实例并运行 '''
    ai = AlienInvasion()
    ai.run_game()