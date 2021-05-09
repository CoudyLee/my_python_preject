import json
import copy

import sign_in
import register

程序状态 = True
step = 1
userdata = {}
username = {'name':''}
password = {'pass':''}

while 程序状态:
    if step == 1:
        用户行为 = int(input('请选择您的操作：1登陆，2注册\n'))
        if 用户行为 == 1:
            step = 2
            pass
        elif 用户行为 ==2:
            step = 3
            pass
        else:
            print('输入错误，请重新输入。\n')
            pass

    elif step == 2:
        if sign_in.userinput(username,password):
            if sign_in.sign_in(username,password,userdata):
                step = 4
                print(f'欢迎回来 {userdata["username"]}')
            else:
                pass
            pass
        else:
            step = 1
        
    elif step == 3:
        if register.userinput(username,password):
            if register.user_register(username,password,userdata):
                step = 4
                print(f'欢迎注册 {userdata["username"]}')
            
        else:
            step = 1

    elif step == 4:
        a = int(input('请输入你想要的操作编号：1退出登录，任意输入退出程序'))
        if a==1:
            step = 1
        else:
            程序状态 = False