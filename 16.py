# 判斷三角形並找最大/最小面積

# 給定n個三角形和其三邊長，輸出該三角形類型，若可構成三角形則再輸出面積。全部輸入完後，再輸出其中最大和最小面積。輸出面積四捨五入取到小數點第二位。

# 若輸入的所有三角形皆不是三角形，則不輸出最大與最小面積，改為輸出 All inputs are not triangles!

# ※三角形面積可利用海龍公式計算(a,b,c表示三角形三邊長)：

# ※三角形類型輸出如下
# 1. 不能成為三角形：輸出not a triangle，且不用輸出面積。
# 2. 正三角形：輸出equilateral triangle。
# 3. 等腰三角形：輸出isosceles triangle。
# 4. 鈍角三角形:輸出obtuse triangle。
# 5. 銳角三角形:輸出acute triangle。
# 6. 直角三角形:輸出right triangle。

# 當三個邊長能構成三角形時，判斷該三角形是否為正三角形，若否，則判斷是否為等腰三角形。若皆非正三角形或等腰三角形，再判斷該三角形為鈍角三角形、銳角三角形或直角三角形。

# 1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於0。
# 2. 正三角形：三個邊相等。
# 3. 等腰三角形：任兩邊相等，且平方和大於第三邊的平方。
# 4. 鈍角三角形: 最長邊平方大於兩短邊平方和
# 5. 銳角三角形: 最長邊平方小於兩短邊平方和
# 6. 直角三角形: 最長邊平方等於兩短邊平方和

# ---------------------------------------------------------------------------------------

# 輸入說明
# 第1行：輸入一個正整數，表示接下來將輸入n個三角形的三邊長（2<=n<=10）
# 第2~n+1行：輸入三個正整數，以空白隔開。表示該三角形的三邊長。

# 輸出說明
# 第1~n行：輸出三角形類型。若可構成三角形，則再輸出面積(四捨五入取到小數點第二位)
# ，面積為一浮點數。三角形類型與面積以空白隔開。

# 若輸入有任一個可構成三角形，輸出兩行
# 第n+1行：為一浮點數，表示最大的三角形面積
# 第n+2行：為一浮點數，表示最小的三角形面積

# 若全部輸入皆不可構成三角形，則輸出一行
# 第n+1行：All inputs are not triangles!

# ---------------------------------------------------------------------------------------

# 範例輸入說明:
# 4 #表示接下來將輸入4個三角形
# 3 4 5 #第1個三角形，邊長為3、4、5
# 2 8 6 #第2個三角形，邊長為2、8、6
# 4 4 3 #第3個三角形，邊長為4、4、3
# 3 3 3 #第4個三角形，邊長為3、3、3


import math

total_triangle = int(input())

triangle_list = []

for i in range(total_triangle):
    a, b, c = map(int, input().split())
    triangle_list.append([a, b, c])

def isTriangle(a):
    flag = True
    for i in range(len(a)):
        if a[i] <= 0:
            flag = False
            break
        else:
            current = a[i]
            other_sum = sum(a) - current
            if current >= other_sum: 
                flag = False
                break
    return flag

def getTriangle(a, b, c): 
    arr = [a, b, c]
    if isTriangle(arr):
        sorted_arr = sorted(arr)
        if sorted_arr[0] == sorted_arr[1] == sorted_arr[2]: 
            print('equilateral triangle', end=' ')
        elif sorted_arr[0] == sorted_arr[1] or sorted_arr[1] == sorted_arr[2]:
            if sorted_arr[0] == sorted_arr[1]:
                equal_side = sorted_arr[0]
                other_side = sorted_arr[2]
            else:
                equal_side = sorted_arr[1]
                other_side = sorted_arr[0]
            if (equal_side**2 + equal_side**2) > other_side**2:
                print('isosceles triangle', end=' ')
            else:
                if sorted_arr[2]**2 == sorted_arr[0]**2 + sorted_arr[1]**2:
                    print('right triangle', end=' ')
                elif sorted_arr[2]**2 > sorted_arr[0]**2 + sorted_arr[1]**2:
                    print('obtuse triangle', end=' ')
                else:
                    print('acute triangle', end=' ')
        elif sorted_arr[2]**2 == sorted_arr[0]**2 + sorted_arr[1]**2:
            print('right triangle', end=' ')
        elif sorted_arr[2]**2 > sorted_arr[0]**2 + sorted_arr[1]**2:
            print('obtuse triangle', end=' ')
        elif sorted_arr[2]**2 < sorted_arr[0]**2 + sorted_arr[1]**2:
            print('acute triangle', end=' ')
    else: 
        print('not a triangle')

def getArea(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

area_list = []
for i in range(total_triangle):
    a, b, c = triangle_list[i]
    getTriangle(a, b, c)
    if isTriangle([a, b, c]):
        area = getArea(a, b, c)
        area_list.append(area)
        print(format(area, '.2f'))
    else:
        pass

if area_list:
    max_area = max(area_list)
    min_area = min(area_list)
    print(format(max_area, '.2f'))
    print(format(min_area, '.2f'))
else:
    print("All inputs are not triangles!")