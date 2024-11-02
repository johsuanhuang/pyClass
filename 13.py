# 線條

# 請計算出(L1、L2、L3…Ln)N條線在 X 軸上所涵蓋的長度(不含重複線段)
# 例如: L1(x1,x2)表示L1線段為 X 軸上點 x1 到點 x2 的線
# 依序輸入起點和終點(起點 < 終點)，且較小的起點先輸入

# ---------------------------------------------------------------------------------------

# 輸入說明
# 第一行 : 輸入總共有多少條線段 (整數N, 1 <= N <= 40)
# 第二行 : 輸入 L1 的 x1, x2 座標 (整數M, -20 <= M <= 20)
# 第 三 ~ N 行 : 重複第二行步驟直到Ln也輸入完成

# 輸出說明
# 輸出N條線段所涵蓋的長度 (整數)

# ---------------------------------------------------------------------------------------

# 範例輸入說明:
# 3 (輸入總共有多少條線段)
# -1 1 (L1 的 (x1,x2) 座標為 (-1,1)) -> (最小的起點先輸入，並以空格隔開)
# 0 2 (L2 的 (x1,x2) 座標為 (0,2)) -> (最小的起點先輸入，並以空格隔開)
# 1 3 (L3 的 (x1,x2) 座標為 (1,3)) -> (最小的起點先輸入，並以空格隔開)

# 範例輸出說明:
# 4 (最左邊的點為-1，最右邊的點為3，因此三條線所涵蓋的長度為4)


line_total = int(input())
line_list = []
# line_total = 4
# line_list = [['3', '1'], ['-1', '1'], ['4', '2'], ['6', '9']]

# line_total = 3
# line_list = [[5, 7], [3, 4], [1, 2]]

for i in range(line_total):
    line = input().split()
    line_list.append(line) # [['2', '3']]
    # line_list.extend(line) # ['2', '3']

# for i in range(line_total):
#     line_list[i] = list(map(int, line_list[i]))

for i in range(len(line_list)):
  line_list[i] = [int(j) for j in line_list[i]]
  line_list[i].sort()
  # print(line_list[i])

line_list.sort()

for i in range(len(line_list)):
  for k in range(i+1,len(line_list) ):
    if line_list[k][0] <= line_list[i][1]:
      line_list[i][1] = max(line_list[k][1], line_list[i][1])
      line_list[k] = [0,0]

# print(line_list)

final_list = [tt for tt in line_list if tt != [0,0]]

total_long = 0

for i in range(len(final_list)):
  total_long += (final_list[i][1] - final_list[i][0])

# print(final_list) 
print(total_long)




# re write the code

# total_line = int(input())

# # line_list = [[-7, -1], [-2, 3], [1, 9], [-10, 10]]
# line_list = []

# for i in range(total_line):
#     line = input().split()
#     line = [int(i) for i in line]
#     line.sort()
#     line_list.append(line)

# line_list.sort()

# for i in range(len(line_list)):
#   for kk in range(i+1, len(line_list)):
#     if line_list[i][1] >= line_list[kk][0]:
#       line_list[i][1] = max(line_list[i][1], line_list[kk][1])
#       line_list[kk] = [0,0]

# new_list = [tt for tt in line_list if tt !=[0,0]]

# total = 0

# for i in range(len(new_list)):
#   total += new_list[i][1] - new_list[i][0]

# print(total)