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
        print(f"{area:.2f}")
    else:
        pass

if area_list:
    max_area = max(area_list)
    min_area = min(area_list)
    print(f"{max_area:.2f}")
    print(f"{min_area:.2f}")
else:
    print("All inputs are not triangles!")