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
input1 = float(input("請輸入身高幾公尺 ： "))
input2 = int(input("請輸入體重幾公斤 ： "))

bmi = input2 / (input1 ** 2)


# print(bmi)
# 取此數小數點後第二個數字
flag = int(str(bmi).split('.')[1][1])
if(flag%2 == 0):
    print(format( math.floor(bmi*100)/100.0, '.2f'))
else:
    print(format( math.ceil(bmi*100)/100.0, '.2f'))