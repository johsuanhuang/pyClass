

def myPrint(n, mark): 
    for i in range(n):
      print(mark, end='')

# def myPrintT(N):
#   for i in range(1, N+1):
#     myPrint(N-i, '.') 
#     myPrint(i, '*') 
#     print('')
# myPrintT(4)
# s

# def myPrintY(N):
#   for i in range(1, N+1):
#     myPrint(N+1-i, '*') 
#     myPrint(i-1, '.') 
#     print('')
# myPrintY(4)
# ****
# ***.
# **..
# *...


# def myPrintNN():
#     for i in range(1, 5): # 1, 2, 3, 4
#       for j in range(i, 5):
#           print(j, end='')
#       print('')
# # 1234
# # 234
# # 34
# # 4
# myPrintNN()

# def myPrintN():
#     for i in range(1, 5): # 1, 2, 3, 4
#       for j in range(1, i+1): # 1, 2, 3, 4
#           print(j, end='')
#       print('')
# # 1
# # 12
# # 123
# # 1234
# myPrintN()

# def myPrintK():
#     for i in range(1, 5): # 4 行
#       for j in range(1, 5+1-i): # 1, 2, 3, 4
#           print(j, end='')
#       print('')
# myPrintK()
# 1234
# 123
# 12
# 1


# def myPrintJ():
#     for i in range(4, 0 , -1): # 4 行
#         pp(i)
#         print('')

# def pp(n): 
#     for i in range(1 , n+1):
#       print( i , end='')

# myPrintJ()
# 1234
# 123
# 12
# 1



# def printSquare(n):
#   for i in range(1, n*n+1):
#     print('%3d'%i, end='')
#     if i%n == 0:
#       print() 
# printSquare(4)

# # Q : %3d 有什麼用途?
# # A : %3d 是格式化輸出，表示輸出的數字佔3個位置，不足的位置
# #     補空格

# # 練習 % 的用法
# xx = 123
# yy = 456

# print('%d %d'%(xx, yy)) # 123 456
# print('%d %d'.format(xx, yy)) # 123 456
# print('{}'.format(xx, yy)) # 123
# print('{}'.format(xx)) # 123
# print('{}'.format(yy)) # 456
# print('加總:{}'.format(xx+yy)) # 加總:579
# print('加總:%d'%(xx+yy)) # 加總:579

def main(n=4):
  for i in range(1 , n+1):
      for j in range(n-i, 0, -1):
          print('#', end='')
      for k in range(i, 0, -1):
          print(k-1, end='')
      print('')

main(4)