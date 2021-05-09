
import json
import copy


def userinput(username,password):
	
	password_ok = False

	print('输入".."返回上一层')
	username['name'] = input("请输入账号")
	if username['name']=='..':
		return False

	while password_ok==False:
		password['pass'] = input('请输入密码')
		if password=='..':
			return False
		password2 = input('请再次输入密码')
		if password=='..':
			return False
		if password2!=password['pass']:
			print('请重新输入密码')

		else:
			password_ok = True

	return True
	pass


def user_register(username,password,userdata):
	userfile_link = f'user_jsonfile/{username["name"]}.json'

	try:
		with open(userfile_link) as userfile:
			print('该账号已存在，请登录或更换账号')
			return False
	except FileNotFoundError:
		with open(userfile_link,'w') as userfile:
			with open('user_jsonfile/id_file.txt','r+') as id_file:
				number_txt = ''
				number = 0
				for i in id_file:
					number_txt += i
				number = int(number_txt.strip())
				userdata['id'] = number + 1
				id_file.seek(0)
				id_file.write(f'{userdata["id"]}')

			userdata['username'] = username['name']
			userdata['password'] = password['pass']

			json.dump(userdata,userfile)

			return True