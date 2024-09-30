

name = input("輸入學生名字:")  
id = int(input("輸入學生學號:"))  
ch = int(input("輸入學生國文成績:")) 
cs = int(input("輸入學生計算機概論成績:"))  
cu = int(input("輸入學生計算機程式設計成績:"))  

total = ch + cs + cu
average = total // 3

print(f"Name:{name}")
print(f"ID:{id}")
print(f"Average:{average}")
print(f"Total:{total}")
