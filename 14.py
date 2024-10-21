# 保齡球

# 小明到保齡球館打保齡球,一輪有十局，試算總分，保齡球規則如下:
# (1)每局有10個保齡球瓶，擊倒1個球瓶得1分
# (2)每局最多有兩次投球機會
# (3)當局如果第一球將10個保齡球瓶全部擊倒(稱為strike)，當局只有一次投球機會，
#     此局計分除了10分外，再加上後面兩球擊倒的球瓶數。
# (4)當局如果第一球未將10個保齡球瓶全部擊倒，但加上第二球則將10個保齡球瓶全部擊倒(稱為spare)，
#     此局計分除了10分外，再加上後面一球擊倒的球瓶數。
# (5)當局若兩球都無法將球瓶全部擊倒，此局計分為兩球擊倒的球瓶數。
# (6)第10局如果第一球將球瓶全部擊倒，後面還有2次投球機會。
# (7)第10局如果第二球才將球瓶全部擊倒，後面還有1次投球機會。
# (8)第10局若兩球都無法將球瓶全部擊倒，則結束比賽。
# (9)總分為10局分數總合。

# 輸入說明:
# 第1局第一球分數(int,0~10)
# 第1局第一球分數(上一球為10則省略) (int,和上一球總和最多為10)
# :
# :
# 第9局第一球分數 (int,0~10)
# 第9局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)
# 第10局第一球分數 (int,0~10)
# 第10局第二球分數(上一球為10則省略) (int,和上一球總和最多為10)
# 第一次額外投球分數(第10局投球總分為10才輸入) (int,0~10)
# 第二次額外投球分數(第10局第一球為10才輸入) (int,0~10)

# 輸出說明:
# 總分 (int)

# Example Input 1:
# 5(第1局第一球)
# 5(第1局第二球) (因為spare，第一局分數為該局投球得分加下一次投球分數，為13分)
# 3(第2局第一球)
# 2(第2局第二球)(第二局分數為該局得分，為5分)
# 6(第3局第一球)
# 4(第3局第二球)(因為spare，第三局分數為該局投球得分加下一次投球分數，為20分)
# 10(第4局第一球)(因為strike，第四局分數為該局投球得分加下二次投球分數，為19分)
# 7(第5局第一球)
# 2(第5局第二球)(第五局分數為該局投球得分，為9分)
# 9(第6局第一球)

score = 0

hit_score = []

# 先算打球的球數
for j in range(10):
    each_score = []
    if j < 9:
        each_score.append(int(input()))
        if each_score[0] == 10:
            hit_score.append(each_score)
            continue
        else:
            each_score.append(int(input()))
        hit_score.append(each_score)
    else:
        each_score.append(int(input()))
        if each_score[0] == 10:
            each_score.append(int(input()))
            each_score.append(int(input()))
        else:
            each_score.append(int(input()))
            if sum(each_score) == 10:
                each_score.append(int(input()))
        hit_score.append(each_score)

    # print(each_score)

# 開始計分

for i in range(10):
    if i <9:
        if hit_score[i][0] == 10:
            if len(hit_score[i+1]) == 2: 
                score += 10 + hit_score[i+1][0] + hit_score[i+1][1]
            else:
                if i + 2 < len(hit_score):
                    score += 10 + hit_score[i+1][0] + hit_score[i+2][0]
                else:
                    # 第9局 Strike，直接取第10局的前兩球
                    score += 10 + hit_score[i+1][0] + hit_score[i+1][1]
        elif sum(hit_score[i]) == 10:
            score += 10 + hit_score[i+1][0]
        else:
            score += sum(hit_score[i])
    else: # 第10局
        score += sum(hit_score[i])

# print(hit_score)
print(score)