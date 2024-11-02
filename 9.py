# 請計算出 a,b,c 三條線在 X 軸上所涵蓋的長度(不含重複線段)

# 例如: a(x1,x2)表示 a 線段為 X 軸上點 x1 到點 x2 的線
# 依序輸入起點和終點(起點 < 終點)，且較小的起點先輸入

# ---------------------------------------------------------------------------------------

# 輸入說明
# 第一行 : 輸入 a 的 x1 座標 (整數, -20 ~ 20)
# 第二行 : 輸入 a 的 x2 座標 (整數, -20 ~ 20)
# 第三行 : 輸入 b 的 x1 座標 (整數, -20 ~ 20)
# 第四行 : 輸入 b 的 x2 座標 (整數, -20 ~ 20)
# 第五行 : 輸入 c 的 x1 座標 (整數, -20 ~ 20)
# 第六行 : 輸入 c 的 x2 座標 (整數, -20 ~ 20)

# 輸出說明
# 輸出三條線段所涵蓋的長度 (整數)

# ---------------------------------------------------------------------------------------

# 範例輸入說明:
# -1 (a 的 x1 座標為 -1) -> A Line起點 : -1 (最小的起點，先輸入)
# 1 (a 的 x2 座標為 1)
# 0 (b 的 x1 座標為 0) -> B Line起點 : 0 (次之)
# 2 (b 的 x2 座標為 2)
# 1 (c 的 x1 座標為 1) -> C Line起點 : 1 (最後輸入)
# 3 (c 的 x2 座標為 3)

# 範例輸出說明:
# 4 (最左邊的點為-1，最右邊的點為3，因此三條線所涵蓋的長度為4)


input_ax1 = int(input())
input_ax2 = int(input())
input_bx1 = int(input())
input_bx2 = int(input())
input_cx1 = int(input())
input_cx2 = int(input())

line_list = []
# line_list = [ [1, 3], [5, 6],[-2, 2]]

line_list.append([input_ax1, input_ax2])
line_list.append([input_bx1, input_bx2])
line_list.append([input_cx1, input_cx2])
line_list.sort()

# print(line_list)

total_length = 0


start_num = line_list[0][0]
end_num = line_list[0][1]

# 比線
for i in range(1, len(line_list)):
    compare_1 = line_list[i][0]
    compare_2 = line_list[i][1]
    # print(compare_1, compare_2)
    if compare_1 <= end_num: # 確定有重疊，因為被比較的現地起點小於上一線的終點
        end_num = max(end_num, compare_2)
    else:
        # 比完了，沒有重疊，那就開始計算
        total_length += end_num - start_num
        # 算完了，那就將沒有重複的起始結束設定起來
        start_num = compare_1
        end_num = compare_2 # 重置，接到71行


total_length += end_num - start_num
print(total_length)





# re write the code


a_x1 = -7
a_x2 = 4
b_x1 = -6
b_x2 = -3
c_x1 = 1
c_x2 = 2


line_list = [[a_x1, a_x2], [b_x1, b_x2], [c_x1, c_x2]]

line_list.sort()

total_length = 0
start_num = line_list[0][0]
end_num = line_list[0][1]

for i in range(len(line_list)):
    line_list[i].sort()
    # print(line_list[i])
    for j in range(i+1, len(line_list)):
        # print(j)
        if line_list[i][1] >= line_list[j][0]:
            end_num = max(end_num, line_list[j][1])
        else:
            total_length += end_num - start_num
            start_num = line_list[j][0]
            end_num = line_list[j][1]



print(total_length)