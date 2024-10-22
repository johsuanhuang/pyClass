import math

total_people = int(input())
bmi_list = []

for i in range(total_people):
    height, weight = map(float, input().split())
    bmi = weight / (height ** 2)
    # 避免精度問題
    temp_bmi = int(bmi * 1000 + 1e-8)
    two_num = int(temp_bmi // 10)
    three_num = int(temp_bmi % 10)

    if three_num > 5:
        two_num += 1
    elif three_num == 5:
        if two_num % 2 != 0:
            two_num += 1


    bmi = two_num / 100
    bmi_list.append(bmi)

max_bmi = max(bmi_list)
min_bmi = min(bmi_list)

print(format(max_bmi, '.2f'))
print(format(min_bmi, '.2f'))


bmi_list.sort()
n = len(bmi_list)
if n % 2 == 0:
    center = (bmi_list[n // 2 - 1] + bmi_list[n // 2]) / 2
else:
    center = bmi_list[n // 2]


temp_center = center * 1000
two_num_center = int(temp_center // 10)
three_num_center = int(temp_center % 10)

if three_num_center > 5:
    two_num_center += 1
elif three_num_center == 5:
    if two_num_center % 2 != 0:
        two_num_center += 1
# 如果 three_num_center < 5，不變

center = two_num_center / 100

print(format(center, '.2f'))


frequency = {}

for i in bmi_list:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

mode = None
max_frequency = 0

for key, value in frequency.items():
    if value > max_frequency:
        max_frequency = value
        mode = key
    elif value == max_frequency:
        if key < mode:
            mode = key

print(format(mode, '.2f'))
