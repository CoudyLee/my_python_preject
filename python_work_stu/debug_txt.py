import copy
import json

a = {}
b = {}
c = {}
d = {}
e = {}
f = {}

def debug(a,b,c,d,e,f):
    with open('user_project/user_jsonfile/coudy.json')as jsonfile:
        a = json.load(jsonfile)
        e = a
        c = copy.copy(a)
        d = copy.deepcopy(a)
        for key in a:
            e[key] = a[key]
        
        qqq = {'4':a}
        fuck = {'1':2,'2':qqq}
        for key in fuck:
            f[key] = fuck[key]

        #print(id(a))
        print(id(e))


print(id(e))
#print(id(a))
debug(a,b,c,d,e,f)
#print(id(a))
print(id(e))
print(e)
print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n')

x ='2'
y ='3'
z = '2'
o = '3'
print(id(x))
print(id(y))
print(id(z))
print(id(o))

x = x + y
print(id(x))

z += o
print(id(z))