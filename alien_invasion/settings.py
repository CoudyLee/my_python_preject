class Settings:
    ''' 游戏设置类 '''
    def __init__(self):
        ''' 初始化游戏设置 '''
        
        #屏幕设置
        self.screen_width = 1200        #画布宽度
        self.screen_height = 800        #画布高度
        self.bg_color = (230,230,230)   #画布颜色

        #飞船设置
        self.ship_limit = 3             #飞船数量

        #子弹设置
        self.bullet_width = 3           #子弹矩形宽度
        self.bullet_height = 15         #子弹矩形高度
        self.bullet_color = (60,60,60)  #子弹颜色
        self.bullet_allowed = 3         #子弹总数

        #外星人设置
        self.fleet_drop_speed = 10.0    #外星人下移速度

        #提高外星人等级加速度和分值增量
        self.speedup_scale = 1.1        #外星人加速度
        self.score_scale = 1.5          #分数增量

        #调用游戏设置方法
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' 重置游戏设置 '''
        self.ship_speed = 1.5           #飞船速度
        self.bullet_speed = 1.0         #子弹速度
        self.alien_speed = 0.1          #外星人速度
        self.fleet_direction = 1        #外星人移动方向（1右，-1左）
        self.alien_points = 50          #外星人分数

    def increase_speed(self):
        ''' 提高游戏节奏 '''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)