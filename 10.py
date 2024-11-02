# 小明到保齡球館打保齡球,一輪有十局,假設小明一到八局都拿零分,剩下最後兩局 ，試算總分，保齡球規則如下:

# (1)每局有10個保齡球瓶，擊倒1個球瓶得1分
# (2)每局最多有兩次投球機會
# (3)當局如果第一球將10個保齡球瓶全部擊倒(稱為strike)，當局只有一次投球機會，此局計分除了10分外，再加上後面兩球擊倒的球瓶數。
# (4)當局如果第一球未將10個保齡球瓶全部擊倒，但加上第二球則將10個保齡球瓶全部擊倒(稱為spare)，此局計分除了10分外，再加上後面一球擊倒的球瓶數。
# (5)當局若兩球都無法將球瓶全部擊倒，此局計分為兩球擊倒的球瓶數。
# (6)第10局如果第一球將球瓶全部擊倒，後面還有2次投球機會。
# (7)第10局如果第二球才將球瓶全部擊倒，後面還有1次投球機會。
# (8)第10局若兩球都無法將球瓶全部擊倒，則結束比賽。
# (9)總分為10局分數總合。

# -----------------------------------------------------------------------------------------------------------------------

# 輸入說明:
# 第9局第一球分數 (int,0~10)
# 第9局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)
# 第10局第一球分數 (int,0~10)
# 第10局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)
# 第一次額外投球分數(第10局投球總分為10才輸入) (int,0~10)
# 第二次額外投球分數(第10局第一球為10才輸入) (int,0~10)
# 輸出說明:
# 總分 (int)

# ---------------------------------------------------------------------------------------------------------------------

# 範例輸入說明
# 5(第9局第一球)
# 5(第9局第二球)
# 10(第10局第一球)
# 0(因為第10局第一次就全倒，第一次額外投球)
# 8(因為第10局第一次就全倒，第二次額外投球)

# 範例輸出說明
# 34(第9局兩次全倒，分數為5+5+10=20。第10局一次全倒，分數為10+0+8=18。總分為20+18=38)


score = 0

hit_num_9 = []
hit_num_10 = []
total_bottle = 10

for j in range(2):
  hit_num_9.append(int(input()))
  if 10 in hit_num_9:
    break

hit_num_10.append(int(input()))
if hit_num_10[0] == 10:
    hit_num_10.append(int(input()))
    hit_num_10.append(int(input()))
else:
    hit_num_10.append(int(input()))
    if sum(hit_num_10) == 10:
        hit_num_10.append(int(input()))

# print(hit_num_9)
# print(hit_num_10)


if hit_num_9[0] == 10:
  score +=  hit_num_9[0]
  score += (hit_num_10[0] + hit_num_10[1])
elif hit_num_9[0] + hit_num_9[1] == 10:
  score += (hit_num_9[0] + hit_num_9[1])
  score += hit_num_10[0]
else:
  score += sum(hit_num_9)

score += sum(hit_num_10)


print(score)
    


# # re write the code

# hit_num_9 = [3, 1]      # 第九局兩球分數
# hit_num_10 = [10, 1, 3] # 第十局第一球strike，包含一次額外投球

# # 無額外投球


# # for i in range(2):
# #   hit_num_9.append(int(input()))
# #   if 10 in hit_num_9:
# #     break

# # hit_num_10.append(int(input()))

# # if hit_num_10[0] == 10:
# #     hit_num_10.append(int(input()))
# #     hit_num_10.append(int(input()))
# # else:
# #     hit_num_10.append(int(input()))
# #     if sum(hit_num_10) == 10:
# #       hit_num_10.append(int(input()))
# score = 0

# if hit_num_9[0] == 10:
#   score +=  hit_num_9[0]
#   score += (hit_num_10[0] + hit_num_10[1])
# elif sum(hit_num_9) == 10:
#   score += (hit_num_9[0] + hit_num_9[1])
#   score += hit_num_10[0]

# else:
#   score += sum(hit_num_9)


# score += sum(hit_num_10)

# print(score)

