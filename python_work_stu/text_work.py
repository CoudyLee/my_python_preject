from text_work_function import get_formatted_name

print('输入‘q’退出程序')

while True:
    first = input('\n输入姓：')
    if first == 'q':
        break
    last = input('输入名：')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f'\tNeatly formatted name: {formatted_name}.')