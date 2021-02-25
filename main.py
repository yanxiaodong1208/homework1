# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 猜数字

import random
from prettytable import PrettyTable

table = PrettyTable(['数字', '结果'])
numRange = random.randint(0, 100)
print("numRange:", numRange)
while 1:
    num = input("enter:")
    num = int(num)
    if numRange > num:
        print(num, "小了")
        table.add_row([num, '小了'])

    elif numRange < num:
        print(num, "大了")
        table.add_row([num, '大了'])

    else:
        print(num, "对了")
        table.add_row([num, '对了'])
        break
print(table)


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
