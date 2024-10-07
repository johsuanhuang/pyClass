# set() 用法
# a = set([1, 2, 3, 4, 5])
# b = set([4, 5, 6, 7, 8])
# print(a & b)  # {4, 5}
# print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8}
# print(a - b)  # {1, 2, 3}
# print(a ^ b)  # {1, 2, 3, 6, 7, 8}



# format 的幾種用法
# print(format(1.2345678, '.2f'))  # 1.23
# print(format(1.2345678, '.3f'))  # 1.235
f = 1.234
# print(format(f, '.2f'))  # 1.23
# print(f'{123.445: .2f}')
# print(f'{123.455: .2f}')
print( not 3<7)

s = "hello"
# s[0] = 'H'  # 這將導致錯誤
t = 123456
# 正確的做法
s = 'H' + s[1:]
# print(s[1:])  #
# print([1, 2, 3][1:])  # [2, 3]
# print([t])
# 將t變成一個list，並切割所有t當中的數字 123456 =>[1, 2, 3, 4, 5, 6]
# print([int(i) for i in str(t)])
# print(int(i) for i in str(t)) # <generator object <genexpr> at 0x7f8b1c7b3d60>


# 算書的價格
a_discount = { 31 : 0.8, 21 : 0.9, 11 : 0.95, 1 : 1}
b_discount = { 31 : 0.85, 21 : 0.95, 11 : 0.98, 1 : 1}

a_num = 27
b_num = 15

a_price = 100
b_price = 150

a_total = a_num * a_price
b_total = b_num * b_price

a_discount_rate = 0
b_discount_rate = 0

for i in a_discount:
    if a_num >= i:
        a_discount_rate = a_discount[i]
        break

for i in b_discount:
    if b_num >= i:
        b_discount_rate = b_discount[i]
        break

a_total *= a_discount_rate
b_total *= b_discount_rate

print(a_total, b_total)


# ss = 70

# if ss>100 or ss < 0 :
#   print("error")
# elif ss >= 80:
#   print("A")
# elif ss >= 70:
#   print("B")
# elif ss >= 60:
#   print("C")
# else:
#   print("F")

# a = 1
# b = 2
# print(f"a = {a}, b = {b}")  # 調試訊息


# 運算符的優先級
# 1. () , [], {} , eg. a = (1 + 2) * 3
# 2. ** , eg. a = 2 ** 3, 2的3次方
# 3. * / %, eg. a = 2 * 3
# 4. + -
# 5. < <= > >= == !=
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= %= **=
# 10. is
# 11. in
# 12. not in
# 13. & | ^ ~ << >>

# # 1. 算術運算
# print(5 + 3)  # 8
# print(5 - 3)  # 2
# print(5 * 3)  # 15
# print(5 / 3)  # 1.6666666666666667
# print(5 // 3)  # 1
# print(5 % 3)  # 2
# print(5 ** 3)  # 125
# # 2. 比較運算
# print(5 > 3)  # True
# print(5 < 3)  # False
# print(5 >= 3)  # True
# print(5 <= 3)  # False
# print(5 == 3)  # False
# print(5 != 3)  # True
# # 3. 邏輯運算
# print(not True)  # False
# print(True and False)  # False
# print(True or False)  # True

# # 4. 位元運算
# print(5 & 3)  # 1
# print(5 | 3)  # 7
# print(5 ^ 3)  # 6
# print(~5)  # -6
# print(5 << 1)  # 10
# print(5 >> 1)  # 2
# # 5. 三元運算
# a = 5
# b = 3
# c = a if a > b else b, 意思是如果a>b為真，則c=a，否則c=b
# print(c)  # 5
# # 6. 成員運算
# a = [1, 2, 3]
# print(1 in a)  # True
# print(4 not in a)  # True
# # 7. 身份運算
# a = 5
# b = 5
# print(a is b)  # True
# print(a is not b)  # False

# # 8. 字串運算
# a = "Hello"
# b = "World"
# print(a + b)  # HelloWorld
# print(a * 3)  # HelloHelloHello
# print("H" in a)  # True
# print("H" not in a)  # False
# # 9. 列表運算
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)  # [1, 2, 3, 4, 5, 6]
# print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(1 in a)  # True
# print(4 not in a)  # True
# # 10. 元組運算
# a = (1, 2, 3)
# b = (4, 5, 6)
# print(a + b)  # (1, 2, 3, 4, 5, 6)
# print(a * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# print(1 in a)  # True
# print(4 not in a)  # True

# # 11. 字典運算
# a = {"name": "Tom", "age": 18}






# % 的各種用法
# %s: 字串
# print("I'm %s" % "Tom")
# # %d: 整數
# print("I'm %d years old" % 18)
# # %f: 浮點數
# print("I'm %.2f meters tall" % 1.75)
# # %x: 十六進位整數
# print("I'm %x years old" % 18)
# # %o: 八進位整數
# print("I'm %o years old" % 18)
# # %e: 科學記號
# print("I'm %e years old" % 18)
# # %c: 字元
# print("I'm %c years old" % 1432)
# # %r: 字串
# print("I'm %r years old" % "Tom")
# # %%: 百分比
# print("I'm %d%% years old" % 18)


