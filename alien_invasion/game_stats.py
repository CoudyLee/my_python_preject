class GameStats:
    ''' 跟踪游戏统计信息 '''

    def __init__(self,ai_game):
        ''' 初始化统计信息 '''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        #self.high_score = 0             #最高得分

        #检测是否有记录文件，有则读取，没有就创建
        try:
            with open('high_score.txt')as f:
                self.high_score = int(f.readline())
        except FileNotFoundError:
            self.high_score = 0
            with open('high_score.txt','w')as f:
                f.write(f'{self.high_score}')

    def reset_stats(self):
        ''' 初始化可重置的统计信息 '''
        self.ships_left = self.settings.ship_limit  #初始化飞船数量
        self.score = 0                              #初始化分数
        self.level = 1                              #初始化等级