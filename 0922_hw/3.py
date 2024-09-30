# 分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

# 結果須輸出到小數點第二位
# print("%.2f" %ans)
# 第一行輸出Sum:num1+num2
# 第二行輸出Difference:num1-num2
# 第三行輸出Product:num1*num2
# 第四行輸出Quotient:num1/num2

input1 = float(input(""))
input2 = float(input(""))


def sum(num1, num2):
    print("Sum:%.2f" % (num1 + num2))

def diff(num1, num2):
    print("Difference:%.2f" % (num1 - num2))

def product(num1, num2):
    print("Product:%.2f" % (num1 * num2))

def quotient(num1, num2):
    print("Quotient:%.2f" % (num1 / num2))

sum(input1, input2)
diff(input1, input2)
product(input1, input2)
quotient(input1, input2)