# BMI = 體重(公斤) / (身高*身高)(公尺)

# 【輸入參數資料型態與類別說明】
# 1.身高(float, 公尺)
# 2.體重(Integer, 公斤)


# 【輸出參數資料型態與類別說明】
# 1.結果須輸出到小數點第二位，print(format(bmi, '.2f'))
# 2.第三位按照四捨六入五看偶規則進行數字簡化
# 四捨六入五看偶規則:
# 保留位數的後一位如果是5，要根據應看尾數「5」的前一位決定是捨去還是進入，如果是奇數則進位，
# 如果是偶數則捨去。例如5.215保留兩位小數為5.22，而 5.225保留兩位小數為5.22。

import math
input1 = float(input(""))
input2 = int(input(""))

bmi = input2 / (input1 ** 2)
tBmi = bmi * 1000
temp_int = int(tBmi + 0.000001) 

second = (temp_int // 10) % 10  # 2
third = temp_int % 10  # 3

# # print(bmi)
ans = float(0)

if(third > 5 ):
    ans = math.ceil(bmi*100)/100.0
elif(third < 5):
    ans = math.floor(bmi*100)/100.0
else:
    if(second % 2 == 0):
        ans = math.floor(bmi*100)/100.0
    else:
        ans = math.ceil(bmi*100)/100.0

print(format(ans, '.2f'))
