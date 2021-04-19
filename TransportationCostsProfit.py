###描画用###
import matplotlib.pyplot as plt
Con1 = []
Con2 = []
Ax = [i for i in range(21)]
############

TeleIn = 175        #テレワーク手当
CPass = int(input("定期代を入力してください: "))
TicketIn = int(input("支給される交通費の片道分を入力してください: "))
TicketOut = int(input("実際にかかる交通費の片道分を入力してください: "))
TwoDays = int(input("交通費を伴う泊まり勤務回数を入力してください: "))
Good1 = [(0,0,0), (0,0,0), (0,0,0)]
Good2 = [(0,0,0), (0,0,0), (0,0,0)]

###オンサイト出勤の回数とテレ出勤の回数毎の契約内容別収支を表示###
for i in range(21):                 #月20日分の出勤をする場合の21パターン
    OnSite = i                      #往復回数(オンサイト出勤回数)
    TeleWork = 20 - OnSite          #テレワーク出勤回数
    
    ###(1), (2)各契約内容での収入・支出###
    Income1 = OnSite * 2 * TicketIn + TeleIn * TeleWork
    if OnSite < 15:
        Income2 = OnSite * 2 * TicketIn
    else:
        Income2 = CPass
    ###現状では支出を区別する必要はない
    if OnSite >= TwoDays * 2:
        Outgo1 = min((OnSite - TwoDays * 2) * 2 * TicketOut + TwoDays * 2 * TicketOut, CPass)
        Outgo2 = min((OnSite - TwoDays * 2) * 2 * TicketOut + TwoDays * 2 * TicketOut, CPass)
    else:
        Outgo1 = min(OnSite * 2 * TicketOut, CPass)
        Outgo2 = min(OnSite * 2 * TicketOut, CPass)
    InOut1 = Income1 - Outgo1
    InOut2 = Income2 - Outgo2
    
    ###整形のため桁数調整してるだけ###
    if OnSite < 10:
        OnSite = "0" + str(OnSite)
    if TeleWork < 10:
        TeleWork = "0" + str(TeleWork)

    ###収支の良い例を格納###
    if Good1[-1][2] < InOut1:
        Good1.pop()
        Good1.append((OnSite,TeleWork,InOut1))
        Good1.sort(reverse=True, key=lambda x:x[2])
    elif Good1[-1][2] == InOut1:
        Good1.append((OnSite,TeleWork,InOut1))
        Good1.sort(reverse=True, key=lambda x:x[2])
    if Good2[-1][2] < InOut2:
        Good2.pop()
        Good2.append((OnSite,TeleWork,InOut2))
        Good2.sort(reverse=True, key=lambda x:x[2])
    elif Good2[-1][2] == InOut2:
        Good2.append((OnSite,TeleWork,InOut2))
        Good2.sort(reverse=True, key=lambda x:x[2])

    ###グラフ描画用###
    Con1.append(InOut1)
    Con2.append(InOut2)
    ##################
    
    print("往復数: " + str(OnSite), "|テレ数: " + str(TeleWork), "|収支(1): " +str(Income1) + "-" + str(Outgo1) + " = " + str(InOut1), "|収支(2): " + str(Income2) + "-" + str(Outgo2) + " = " + str(InOut2))

###収支の良い例を表示###
print("収支(1)の上位3例は以下のとき")
for p,q,r in Good1:
    print("往復数: " +str(p)+ "|テレ数: " +str(q)+ "収支: +" +str(r))
print("収支(2)が上位3例は以下のとき")
for p,q,r in Good2:
    print("往復数: " +str(p)+ "|テレ数: " +str(q)+ "収支: +" +str(r))

####グラフ描画###
plt.plot(Ax, Con1, marker="o", color = "red", linestyle = "--")
plt.plot(Ax, Con2, marker="v", color = "blue", linestyle = ":")
plt.title("TransporTwoDaystion Costs Profit  Red=1, Blue=2")
plt.xlabel("On-site")
plt.ylabel("Profit")
plt.show()
################

###コマンドプロンプトの即終了阻止用###
input("エンターを押すと終了します")