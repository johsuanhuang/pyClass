# BMI比較

# 給定n個人輸入身高與體重並計算BMI，BMI計算後需先四捨六入五看偶
# 取到小數點第二位，
# 並以捨入後的結果計算BMI的最大值、最小值、中位數、眾數。
# ※BMI = 體重(公斤) / (身高*身高)(公尺)

# ※四捨六入五看偶規則
# 保留位數的後一位如果是5，要根據應看尾數「5」的前一位決定是捨去還是進入，
# 如果是奇數則進位，如果是偶數則捨去。例如5.215保留兩位小數為5.22，
# 而 5.225保留兩位小數為5.22。

# ※中位數：為一數列經過排序後，處數列中間的數，如：
# [3,6,8,10,11] 則中位數 = 8
# 若數列有偶數個數，則取中間兩數的平均為中位數，如：
# [2,3,5,8,13,21] 則中位數 = (5+8)/2 = 6.5
# ※眾數：為一數列當中出現最多次的數。如：
# [1,2,2,3,3,3,4,4,5] 則眾數 = 3
# 若有多個眾數，則取最小者做為眾數。如：
# [2,2,2,3,3,3,4,4] 則眾數 = 2

# ________________________________________

# 輸入說明
# 第1行：輸入一個整數，表示接下來將輸入n個人的身高體重（2<=n<=10）　
# 第2~n+1行：輸入兩個浮點數，以空白隔開。第一個浮點數為身高(公尺，
# 1.50<=身高<=2.50)，第二個浮點數為體重(公斤，0.0<=體重<=150.0)。

# 輸出說明
# 第1行：輸出為一浮點數，表示n個人中BMI的最大值
# 第2行：輸出為一浮點數，表示n個人中BMI的最小值
# 第3行：輸出為一浮點數，表示n個人中BMI的中位數
# 第4行：輸出為一浮點數，表示n個人中BMI的眾數

# ________________________________________

# Example Input 1:
# 4 #表示接下來將有4筆輸入
# 1.78 75.0 #第1個人，身高=1.78公尺，體重=75.0公斤
# 1.77 84.5 #第2個人，身高=1.77公尺，體重=84.5公斤
# 1.75 62.3 #第3個人，身高=1.75公尺，體重=62.3公斤
# 1.56 48.5 #第4個人，身高=1.56公尺，體重=48.5公斤


import math

total_people = int(input())
bmi_list = []

for i in range(total_people):
    height, weight = map(float, input().split())
    bmi = weight / (height ** 2)
    
    # 轉成整數處理（乘以1000取整數，避免精度問題）
    temp_bmi = int(bmi * 1000)
    two_num = temp_bmi // 10
    three_num = temp_bmi % 10
    
    # 四捨六入五看偶規則
    if three_num > 5:  # 大於5要進位
        two_num += 1
    elif three_num == 5:  # 等於5看前一位奇偶
        if two_num % 2 != 0:  # 奇數進位
            two_num += 1
    # 小於5不變
    
    bmi = two_num / 100
    bmi_list.append(bmi)

max_bmi = max(bmi_list)
min_bmi = min(bmi_list)

print(f"{max_bmi:.2f}")
print(f"{min_bmi:.2f}")

bmi_list.sort()

# 計算中位數
if len(bmi_list) % 2 == 0:
    mid1 = bmi_list[len(bmi_list) // 2 - 1]
    mid2 = bmi_list[len(bmi_list) // 2]
    center = (mid1 + mid2) / 2
    
    # 對中位數進行四捨六入五看偶處理
    temp_center = int(center * 1000)
    two_num = temp_center // 10
    three_num = temp_center % 10
    
    if three_num > 5:
        two_num += 1
    elif three_num == 5:
        if two_num % 2 != 0:
            two_num += 1
            
    center = two_num / 100
else:
    center = bmi_list[len(bmi_list) // 2]

print(f"{center:.2f}")

# 計算眾數
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

print(f"{mode:.2f}")



# re write the code

# import math


# total_people = int(input())

# bmi_list = []

# if total_people<2 or total_people>10:
#   print("輸入範圍錯誤")
#   exit()

# def round_half_even(value):
#     two_num = int(value * 100 % 10)
#     three_num = int(value * 1000 % 10)
#     if three_num == 5:
#         if two_num % 2 == 0:
#             return math.floor(value * 100) / 100
#         else:
#             return math.ceil(value * 100) / 100
#     else:
#         if three_num > 5:
#             return math.ceil(value * 100) / 100
#         else:
#             return math.floor(value * 100) / 100

# for i in range(total_people):
#   tt = input().split()
#   hh = float(tt[0])
#   ww = float(tt[1])
#   bmi = ww/ hh**2

#   two_num = int(bmi * 100 % 10)
#   three_num = int(bmi * 1000 % 10)
#   bmi = round_half_even(bmi)
#   bmi_list.append(bmi)

# max_bmi = max(bmi_list)
# min_bmi = min(bmi_list)

# print('%.2f' %max_bmi)
# print('%.2f' %min_bmi)

# bmi_list.sort()

# # print(bmi_list)



# mid_num = 0

# if len(bmi_list) % 2 == 0:
#   mid_count = len(bmi_list) // 2
#   mid_num = (bmi_list[mid_count] + bmi_list[mid_count-1]) / 2
#   mid_num = round_half_even(mid_num)
# else:
#   mid_count = len(bmi_list) // 2
#   mid_num = bmi_list[mid_count]

# print('%.2f' %mid_num)


# count_num = {}

# for i in bmi_list:
#   if i in count_num:
#     count_num[i] += 1
#   else:
#     count_num[i] = 1


# max_count = 0
# mode = None

# for key, value in count_num.items():
#   if value > max_count: 
#     max_count = value
#     mode = key
#   else:
#     if value == max_count:
#       if key < mode:
#         mode = key

# print('%.2f' %mode)