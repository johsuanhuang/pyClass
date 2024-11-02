# 撲克牌的牌面符號A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K，對應的點數：
# 2~10 點數為 2~10，A, J, Q, K 為 0.5。
# 一位玩家一位莊家，各發三張撲克牌，加總點數越接近 10.5 的贏；
# 如果總點數相同，則雙方平手 (Tie)
# 總點數超過 10.5 (不含10.5) ，點數變為 0。

# 以兩種規則決定勝負：
# 1. 先加總玩家總點數，如果玩家點數為0則不需加總莊家點數，此時莊家獲勝。
# 2. 玩家與莊家總點數都計算完後才判斷勝負。

# -------------------------------------------------------------------

# 輸入說明:
# 第一行，輸入玩家的名字(字串)
# 第二 ~ 四行，輸入玩家的三張撲克牌
# 第五行，輸入莊家的名字(字串)
# 第六 ~ 八行，輸入莊家的三張撲克牌

# 輸出說明:
# 第一行，以第一種規則判斷，輸出「勝利者的名字 Win」，若雙方平手，輸出Tie
# 第二行，以第二種規則判斷，輸出「勝利者的名字 Win」，若雙方平手，輸出Tie

# -------------------------------------------------------------------

# 範例輸入說明:
# X (玩家的 名字 為 X)
# A (玩家的 第一張 撲克牌為 A)
# 9 (玩家的 第二張 撲克牌為 9)
# 3 (玩家的 第三張 撲克牌為 3)
# Y (莊家的 名字 為 Y)
# 6 (莊家的 第一張 撲克牌為 4)
# 8 (莊家的 第二張 撲克牌為 8)
# Q (莊家的 第三張 撲克牌為 Q)

# 範例輸出說明:
# Y Win (以第一種規則判斷：玩家的總點數為0.5 + 9 + 3 = 12.5，
# 因為玩家總點數超過10.5，所以玩家點數變為0，莊家獲勝)
# Tie (以第二種規則判斷，莊家的總點數為 6 + 8 + 0.5 = 14.5，
# 因為玩家與莊家總點數都超過10.5，所以玩家與莊家總點數都變為0，平手)

card_values = {
    'A': 0.5,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 0.5,
    'Q': 0.5,
    'K': 0.5
}


player_name = input()


def read_cards():
    cards = []
    for i in range(3):
        card = input()
        cards.append(card)
    return cards

player_cards = read_cards()


player2_2_name = input()


player_2_2_cards = read_cards()


def calculate_total(cards):
    total = 0
    for card in cards:

        total += card_values.get(card, 0)
    if total > 10.5:
        total = 0
    return total


player_total = calculate_total(player_cards)
dealer_total = calculate_total(player_2_2_cards)

if player_total == 0:
    winner_rule1 = f"{player2_2_name} Win"
else:
    if abs(10.5 - player_total) < abs(10.5 - dealer_total):
        winner_rule1 = f"{player_name} Win"
    elif abs(10.5 - player_total) > abs(10.5 - dealer_total):
        winner_rule1 = f"{player2_2_name} Win"
    else:
        winner_rule1 = "Tie"


if abs(10.5 - player_total) < abs(10.5 - dealer_total):
    winner_rule2 = f"{player_name} Win"
elif abs(10.5 - player_total) > abs(10.5 - dealer_total):
    winner_rule2 = f"{player2_2_name} Win"
else:
    winner_rule2 = "Tie"


print(winner_rule1)
print(winner_rule2)



# re write the code

# player_name = "C"
# player_cards = ["10", "9", "8"]

# dealer_name = "D"
# dealer_cards = ["8", "9", "10"]

# # player_name = input()
# # player_cards = [input() for i in range(3)]

# # dealer_name = input()
# # dealer_cards = [input() for i in range(3)]

# card_values = {
#   'A': 0.5,
#   '2': 2,
#   '3': 3,
#   '4': 4,
#   '5': 5,
#   '6': 6,
#   '7': 7,
#   '8': 8,
#   '9': 9,
#   '10': 10,
#   'J': 0.5,
#   'Q': 0.5,
#   'K': 0.5
# } 

# player_value = sum([card_values[i] for i in player_cards])
# dealer_value = sum([card_values[j] for j in dealer_cards])

# if player_value > 10.5:
#   print(f"{dealer_name} Win")
# else:
#   if dealer_value > 10.5:
#     print(f"{player_name} Win")
#   elif player_value == dealer_value:
#     print("Tie")
#   elif player_value < dealer_value:
#     print(f"{dealer_name} Win")
#   elif player_value > dealer_value:
#     print(f"{player_name} Win")



# if player_value > 10.5 and dealer_value > 10.5:
#   print(f"Tie")
# elif player_value > dealer_value:
#   print(f"{player_name} Win")
# elif dealer_value > player_value:
#   print(f"{dealer_name} Win")
# else:
#   print(f"Tie")