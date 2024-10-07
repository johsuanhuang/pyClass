# 判斷何種三角形
# 當三個邊長能構成三角形時，判斷該三角形是否為正三角形，若否，
# 則判斷是否為等腰三角形。若皆非正三角形或等腰三角形，
# 再判斷該三角形為鈍角三角形、銳角三角形或直角三角形。
# 1. 不能成為三角形：任兩邊和不大於第三邊，或任一邊長不大於0。
# 2. 正三角形：三個邊相等。
# 3. 等腰三角形：任兩邊相等，且平方和大於第三邊的平方。
# 4. 鈍角三角形: 最長邊平方大於兩短邊平方和
# 5. 銳角三角形: 最長邊平方小於兩短邊平方和
# 6. 直角三角形: 最長邊平方等於兩短邊平方和

# 【輸入參數資料型態與類別說明】
# 1.輸入三個整數邊長(int)

# 【輸出參數資料型態與類別說明】
# 1. 不能成為三角形：輸出not a triangle。
# 2. 正三角形：輸出equilateral triangle。
# 3. 等腰三角形：輸出isosceles triangle。
# 4. 鈍角三角形:輸出obtuse triangle。
# 5. 銳角三角形:輸出acute triangle。
# 6. 直角三角形:輸出right triangle。
# 餘弦定理
# a² = b² + c² → 直角三角形
# a² > b² + c² → 鈍角三角形
# a² < b² + c² → 銳角三角形

a,b,c = int(input('輸入第一個整數邊長 : ')), int(input('輸入第二個整數邊長 : ')) , int(input('輸入第三個整數邊長 : '))

def isTriangle(a):
    flag = True
    for  i  in range(len(a)):
        if(a[i] <= 0) : flag =  False
        else :
            current = a[i]
            other_sum = sum(a) - current
            if(current >=other_sum) : flag = False
    return flag

def getTriangle(a, b, c) : 
    arr = [a,b,c]
    if(isTriangle(arr)) :
        sorted_arr = sorted(arr)
        if(sorted_arr[0] == sorted_arr[1] == sorted_arr[2]) : 
            print('正三角形')
        elif(sorted_arr[0] == sorted_arr[1] or sorted_arr[1] == sorted_arr[2]) :
            print('等腰三角形')
        elif(sorted_arr[2]**2 == sorted_arr[0]**2 + sorted_arr[1]**2) :
            print('直角三角形')
        elif(sorted_arr[2]**2 > sorted_arr[0]**2 + sorted_arr[1]*2):
            print('鈍角三角形')
        elif(sorted_arr[2]**2 < sorted_arr[0]**2 + sorted_arr[1]*2):
            print('銳角三角形')
        Í
    else : 
        print('not a triangle')


getTriangle(a,b,c)