# import os windows only
# 第一行，輸入學生名字 
# 第二行，輸入學生學號 
# 第三行，輸入學生國文成績 
# 第四行，輸入學生計算機概論成績 
# 第五行，輸入學生計算機程式設計成績 

name = input("輸入學生名字 : ")  
id = int(input("輸入學生學號 : "))  
ch = int(input("輸入學生國文成績 : ")) 
cs = int(input("輸入學生計算機概論成績 : "))  
cu = int(input("輸入學生計算機程式設計成績 : "))  

total = ch + cs + cu
average = total // 3


#  輸出要有四個項目
print(f"Name:{name}")
print(f"ID:{id}")
print(f"Average:{average}")
print(f"Total:{total}")



# os.system('pause') windows only