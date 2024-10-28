# 課程衝堂

# 給定N門課程資料，檢查課程是否衝堂或輸入錯誤，輸出檢查結果。
# 依序輸入 :
# 課程編號 (科目名稱 + 4位數字)、
# 上課小時數 (1-3 小時)、
# 上課時間 (依小時數輸入上課時間, 星期 1-5, 第 1-9,a,b,c 節)。

# -----------------------------------------------------------------------------------------------

# 輸入說明：
# 第一行，輸入整數N(2 <= N <= 10)
# 接著輸入 N 門課程的資訊，每一門課程的輸入如下：
# 　　第一行，輸入課程名稱及編號(字串)
# 　　第二行，上課小時數，整數 H (1<=H<=3)
# 　　接下來 H 行：
# 　　　　每一行為一個字串，第一個字元表示星期幾，第二個字元表示第幾節

# 輸出說明：
# 輸入有任何錯誤，輸出 -1
# 若無發生衝堂，則輸出correct
# 若發生衝堂，輸出所有衝堂的課程，每次輸出兩個衝堂的課程編號，
# 以及在哪一天的哪一節衝突，參考下列格式 :
# 　　{課程1編號},{課程2編號},{衝堂在哪天哪節}
# 　　先輸入的課程為課程1，後輸入的課程為課程2

# -----------------------------------------------------------------------------------------------

# 範例輸入說明
# 3 (總共有三門課程)
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
# Chinese1001,Math1003,13 (課程Chinese1001跟課程Math1003，
# 在星期1第3節衝堂，因課程Chinese1001先輸入，所以課程Chinese1001放前面)


total_course = int(input())
if total_course < 2 or total_course > 10:
    print(-1)
    exit()
class_list = []
# total_course = 3
# class_list = [['Chinese1001', ['11', '12', '13']], ['English1002', ['21', '22', '23']], ['Math1003', ['31', '32', '13']]]

for i in range(total_course):
    class_name = input()
    # 檢查是否名稱內有四個數字
    if not class_name[-4:].isdigit():
        print(-1)
        break
    class_hour = int(input())
    if class_hour < 1 or class_hour > 3:
        print(-1)
        break
    class_time = []
    for j in range(class_hour):
        # class_time.append(input())
        time_input = input()
        if len(time_input) != 2:
            print(-1)
            exit()
        day = time_input[0]
        period = time_input[1]
        if day not in ['1', '2', '3', '4', '5']:
            print(-1)
            exit()
        if period not in ['1','2','3','4','5','6','7','8','9','a','b','c']:
            print(-1)
            exit()
        class_time.append(time_input)
    class_list.append([class_name, class_time])

# print(class_list)
conflict_found = False  


for i in range(total_course):
    for h in range(len(class_list[i][1])):
        # print(class_list[i][1][h])
        for q in range(i+1, total_course):
            for zz in range(len(class_list[q][1])):
                if class_list[i][1][h] == class_list[q][1][zz]:
                    print(f'{class_list[i][0]},{class_list[q][0]},{class_list[i][1][h]}')
                    conflict_found = True 
                    break


if not conflict_found:
    print('correct')

