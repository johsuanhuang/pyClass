# 最佳資費選擇

# 輸入每月網內、網外、市話、通話時間(秒)及網內、網外簡訊則數、網路流量，求最佳資費。
# 費率如下表：
# 資費類型 183型 383型 983型 1283型
# 月租費 183元 383元 983元 1283元

# 優惠內容月租費可抵等額通信費

# 語音費率 網內 0.08 0.07 0.06 0.05
# (元/秒) 網外 0.139 0.130 0.108 0.100
# (元/秒) 市話 0.135 0.121 0.101 0.090

# 簡訊費率 網內 1.128 1.128 1.128 1.128
# (元/則) 網外 1.483 1.483 1.483 1.483

# 網路流量 1G 3G 5G 吃到飽
# 網路加購價
# (元/G) 250 200 150 無

# 優惠內容月租費可抵等額通信費 :
# 若總通信費(包含通話時間、簡訊數量、網路加購)
# 高於該資費類型的費用，則以原費用進行收費，若低於該資費類型的費用，則以該資費類型的費用進行收費。

# 例如:
# 選擇183型，總通信費為200元，則應繳金額為200元
# 若總通信費為150元，則應繳金額為183元。



# in_sec = int(input('輸入每月網內通話時間(秒) : '))
# out_sec = int(input('輸入每月網外通話時間(秒) : '))
# city_sec = int(input('輸入每月市話通話時間(秒) : '))
# in_sms = int(input('輸入每月網內簡訊則數 : '))
# out_sms = int(input('輸入每月網外簡訊則數 : '))
# net_traffic = int(input('輸入網路流量(GB) : '))
in_sec = int(input(''))
out_sec = int(input(''))
city_sec = int(input(''))
in_sms = int(input(''))
out_sms = int(input(''))
net_traffic = int(input(''))

pay_plan = [183, 383, 983, 1283]

in_sec_rate = { 183 : 0.08, 383 : 0.07, 983 : 0.06, 1283 : 0.05}
out_sec_rate = { 183 : 0.139, 383 : 0.130, 983 : 0.108, 1283 : 0.100}
city_sec_rate = { 183 : 0.135, 383 : 0.121, 983 : 0.101, 1283 : 0.090}
in_sms_rate = { 183 : 1.128, 383 : 1.128, 983 : 1.128, 1283 : 1.128}
out_sms_rate = { 183 : 1.483, 383 : 1.483, 983 : 1.483, 1283 : 1.483}
net_traffic_rate = { 183 : 250, 383 : 200, 983 : 150, 1283 : 0}
net_traffic_gb = { 183 : 1, 383 : 3, 983 : 5, 1283 : 0}

total = 0

# best_plan = None
# best_cost = float('inf')

# 初始化最佳資費
best_plan = 0
best_cost = 0
first = True  # 加入flag來處理第一次比較

for i in pay_plan:
    total = 0
    total += in_sec * in_sec_rate[i]
    total += out_sec * out_sec_rate[i]
    total += city_sec * city_sec_rate[i]
    total += in_sms * in_sms_rate[i]
    total += out_sms * out_sms_rate[i]
    out_range = net_traffic - net_traffic_gb[i]

    # 計算網路費用
    out_range = net_traffic - net_traffic_gb[i]
    if out_range > 0:  # 如果超出免費流量，計算加購費用
        total += out_range * net_traffic_rate[i]

    # 如果通信費用總和超過月租費，則通信費即為總費用，否則為月租費
    total_cost = max(i, total)

    
    if(out_range > 0):
        total += out_range * net_traffic_rate[i]

    #   另一個寫法
    if first:
        best_plan = i
        best_cost = total_cost
        first = False
    else:
        # 更新最小總費用和對應的資費計畫
        if total_cost < best_cost:
            best_cost = total_cost
            best_plan = i
print(round(best_cost))
print(best_plan)

# print(f"最佳資費為: {best_plan}元，總費用為: {best_cost}元")
