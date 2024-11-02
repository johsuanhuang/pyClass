# 請檢查輸入的三門課程是否衝堂。

# 依序輸入 :
# 課程編號 (科目名稱 + 4位數字)、
# 上課小時數 (1-3 小時)、
# 上課時間 (依小時數輸入上課時間, 星期 1-5, 第 1-9,a,b,c 節)。

# -----------------------------------------------------------------------------------------------

# 輸入說明:
# 輸入三門課程的資訊
# 每一門課程的資訊
# 第一行 : 輸入課程編號(字串)
# 第二行 : 上課小時數 H (整數，1<=H<=3)
# 接下來有 H 行
# 每一行為一個字串，第一個字元表示星期幾，第二個字元表示第幾節

# 輸出說明:
# 輸入任何錯誤，輸出 -1
# 若無發生衝堂，則輸出correct

# 若發生衝堂 :
# 輸出所有衝堂的課程，每次輸出兩個衝堂的課程編號，以及在哪一天的哪一節衝突，參考下列格式 :
# {課程1編號},{課程2編號},{衝堂在哪天哪節}
# 先輸入的課程為課程1，後輸入的課程為課程2

# -----------------------------------------------------------------------------------------------

# 範例輸入說明

# Chinese1001 (第一門課課程編號)
# 3 (3小時，每節課1小時)
# 11 (星期1 第1節課)
# 12 (星期1 第2節課)
# 13 (星期1 第3節課)
# English1002 (第二門課課程編號)
# 3 (3小時，每節課1小時)
# 21 (星期2 第1節課)
# 22 (星期2 第2節課)
# 23 (星期2 第3節課)
# Math1003 (第三門課課程編號)
# 3 (3小時，每節課1小時)
# 31 (星期3 第1節課)
# 32 (星期3 第2節課)
# 13 (星期1 第3節課)
# 範例輸出說明 (兩課程編號衝突在哪幾節)
# Chinese1001,Math1003,13 (課程Chinese1001跟課程Math1003，在星期1第3節衝堂，因課程Chinese1001先輸入，所以課程Chinese1001放前面)



input_list = {}
# input_list = {'cccc': ['13', '14', '26'], 'vvvv': ['14', '24', '34'], 'xxxx': ['44', '24', '34']}

for i in range(3):
  class_name = input("")
  class_hours = int(input(""))
  class_date_time = []
  if class_hours < 1 or class_hours > 3:
    print(-1)
    exit()
  for kk in range(class_hours):
    # print(class_hours)
    temp = input("")
    if(len(temp) != 2) or temp[0] not in ['1', '2', '3', '4', '5'] or temp[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']:
      print(-1)
      exit()

    class_date_time.append(temp)
  input_list[class_name] = class_date_time

# print(len(input_list))
# input_list2 = input_list.copy()
print_list = []


key_name = list(input_list.keys())

for g in range(len(input_list)):
  for y in range(g+1,len(input_list)):
    for ss in input_list[key_name[g]]:
      for pp in input_list[key_name[y]]:
        if ss == pp:
          print_list.append([key_name[g], key_name[y], ss])
          break

if print_list:
  for i in print_list:
    # 把鎮列轉成字串
    print(','.join(i))
else:
    print("correct")


# re write the code


# class_list = {
#     'Math1011': ['46'],
#     'Chinese1002': ['45', '46'],
#     'English1003': ['61', '5a']
# }

# class_list = {}


# for i in range(3):
#   class_name = input()
#   class_num = int(input())
#   class_list[class_name] = []

#   if(class_num < 1 or class_num > 3):
#     print(-1)
#     exit()

#   for j in range(class_num):
#     ttt = input()
#     if (len(ttt) != 2) or ttt[0] not in ['1', '2', '3', '4', '5'] or ttt[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c']:
#       print(-1)
#       exit()
#     class_list[class_name].append(ttt)




# class_name = list(class_list.keys())
# print(class_list)
# conflict_list = []

# for i in range(len(class_name)):
#   # print(i)
#   for j in range(i+1, len(class_list)):
#     # print(class_name[i], class_name[j])
#     for kk in class_list[class_name[i]]:
#       # print(kk)
#       for pp in class_list[class_name[j]]:
#         if kk == pp:
#           # print(kk, pp)
#           conflict_list.append([class_name[i], class_name[j], kk])


# if not conflict_list:
#   print("correct")
# else:
#   for i in conflict_list:
#     print(','.join(i))



