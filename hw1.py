import os


# print('\n')
print('print some number')

data = input().split()
data = [int(x) for x in data]
print(max(data), sum(data))

os.system('pause')