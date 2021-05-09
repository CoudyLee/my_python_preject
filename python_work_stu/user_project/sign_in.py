
import json
import copy

def userinput(username,password):
	print('输入".."返回上一层')
	username['name'] = input("请输入账号")
	if username['name'] =='..':
		return False
	password['pass'] = input('请输入密码')
	if password['pass']=='..':
		return False
	return True
	pass

def sign_in(username,password,userdata):
	userfile_link = f'user_jsonfile/{username["name"]}.json'
	try:
		with open(userfile_link) as userfile:
			userdata1 = json.load(userfile)
			for key in userdata1.keys():
				userdata[key] = userdata1[key]

			if userdata['password']!=password['pass']:
				print('你输入的密码错误，请重新输入')
				for key in userdata1.keys():
					del userdata[key]
				return False
			else:
				return True

	except FileNotFoundError:
		print('你的账号输入错误请检查，或者注册账号')
		return False