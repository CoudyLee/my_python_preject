filename = 'debug_file/debug_file_1.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

a = ''
for i in lines:
    a += i.rstrip()

print(a)
print(len(a))

filename = 'debug_file/write_debug_1.txt'

with open(filename,'a') as fuck:
    fuck.write('10')
#    fuck.seek(0)
#    print(fuck.read())
#    fuck.write('10')

