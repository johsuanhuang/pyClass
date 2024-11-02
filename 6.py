# 一元二次方程式

# 一元二次方程式，aX^2 + bx + c = 0，輸入a, b, c, 求方程式的兩個實/虛根。
# T = math.sqrt(b*b-4*a*c)
# 第一個根，x1 = (-b+T)/(2*a)
# 第二個根，x2= (-b-T)/(2*a)

# 本題需 import math
# ---------------------------------------------------

# 輸入說明：
# 第一行，輸入a (Integer)
# 第二行，輸入b (Integer)
# 第三行，輸入c (Integer)

# 輸出說明：
# 當T>=0，輸出x1, x2為實根，輸出到小數點第一位
# 第一行，輸出 print("%.1f” %(x1))
# 第二行，輸出 print("%.1f” %(x2))

# 當T<0，輸出x1 , x2為虛根，輸出到小數點第一位
# 第一行，輸出 print("%.1f+%.1fi" %(x11,x12))
# 第二行，輸出 print("%.1f-%.1fi" %(x21,x22))
# 若x11或x21為0.0時，則不須輸出正負號
import math

a = int(input(""))
b = int(input(""))
c = int(input(""))


# 判別式
D = b*b - 4*a*c


def func(a, b, c):
    if D < 0:
      # print("no 實根")
      rk = -b / (2 * a)
      fake_k = math.sqrt(abs(D)) / (2 * a)
      # math.sqrt(abs(D)) == D**0.5 也可以用 math.sqrt() 來寫

      print("%.1f+%.1fi" % (rk, fake_k))
      print("%.1f-%.1fi" % (rk, fake_k))
    else:  # 有實根
      x1 = (-b + D** 0.5) / (2 * a)
      x2 = (-b - D** 0.5) / (2 * a)

      print("%.1f" % x1)
      print("%.1f" % x2)


func(a, b, c)


# re write

# a, b, c = 2,0,2


# D = b**2 - 4*a*c

# # print(D)

# if D >= 0:
#     x1 = (-b + D**0.5) / (2*a)
#     x2 = (-b - (D**0.5)) /  (2*a)
#     print('%.1f' % x1)
#     print('%.1f' % x2)
# else :
#     rr = -b / (2*a)
#     ll = abs(D)**0.5 / (2*a)
#     print('%.1f+%.1fi' % (rr,ll))
#     print('%.1f-%.1fi' % (rr,ll))

