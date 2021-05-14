import pygame.font

class Button:
    ''' 按钮类 '''
    def __init__(self,ai_game,msg):
        ''' 初始化按钮 '''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #设置按钮样式
        self.width,self.height = 200,50             #按钮长和宽
        self.button_color = (0,255,0)               #按钮颜色
        self.text_color = (255,255,255)             #字体颜色
        self.font = pygame.font.SysFont(None,48)    #字体和大小

        #创建按钮矩形
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        print(self.rect)
        #按钮文本内容
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        ''' 将文本渲染成图像，并放在按钮上居中 '''
        self.msg_image = self.font.render(
            msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center#中心点

    def draw_button(self):
        ''' 渲染按钮 '''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
