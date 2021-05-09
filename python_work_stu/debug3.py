import json

filename = 'debug_file/jsonfile/numbers.json'

numbers = [1,2,3,4,5,6,7,8,9,10]

with open(filename,'w') as a:
    json.dump(numbers,a)


numbers2 = []
number = 0
with open(filename) as a:
    numbers2 = json.load(a)
    for i in numbers2:
        number += i

print(number)