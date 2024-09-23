# 一元二次方程式，ax^2 + bx + c = 0，輸入a, b, c, 求 方程式的兩個實根。


a = int(input("請輸入a : "))
b = int(input("請輸入b : "))
c = int(input("請輸入c : "))


# 判別式
D = b*b - 4*a*c


def func(a, b, c):
    if D < 0:
      print("no 實根")
    else:  # 有實根
      x1 = (-b + D** 0.5) / (2 * a)
      x2 = (-b - D** 0.5) / (2 * a)

      # str.format() 方法
      # print("x1: {:.1f}".format(x1))
      # print(format(x1, ".1f"))
      # f-string 格式化（新式方法）
      # print(f"{x1:.1f}") 

      # printf-style 格式化（舊式方法）
      print("%.1f" % x1)
      print("%.1f" % x2)


func(a, b, c)


# 格式說明符 
# x = 3.14159
# print("Pi 的值是 %.2f" % x) 
# print("Pi 的值是 %d" % x)
# print("Pi 的值是 %s" % x)
# %s：字符串
# %d：整數
# %f：浮點數
# %.1f：浮點數，保留一位小數
# 其他還有 %x（十六進位）、%o（八進位）等等。 