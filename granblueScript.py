import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import pyautogui
import time
import random
import webbrowser
from tkinter import messagebox


#グランブルーファンタジーというゲームの素材獲得系の試練を周回する用のスクリプトプログラムgit

def AP_AA_FC():
    i = True
    while i:

        time.sleep(1.4)

        if pyautogui.locateCenterOnScreen('Notap.png', confidence=0.5):
            #pyautogui.moveTo(401,661,1.5)
            #pyautogui.click()
    ##汁数決定(検証中)
            #pyautogui.moveTo(405,298,1.5)
            #pyautogui.click()
    ##回復する(検証中)
            pyautogui.moveTo(421,740,1.5)
            pyautogui.click()
    ##オーケーbutton
            pyautogui.moveTo(300,700,1.5)
            pyautogui.click()

        #Shokanseki
        time.sleep(0.5)
        pyautogui.moveTo(322, 473, 1.8)
        pyautogui.click()
        #OKButton
        pyautogui.moveTo(419, 716, 1.8)
        pyautogui.click()
        #autoAttack
        time.sleep(1.25)
        pyautogui.click()


        #"フォールスチェック画面下部にカーソル移動"
        pyautogui.moveTo(947,680)

        time.sleep(3)
        i = False
            #if文は必ずしも比較する必要がない↓↓


        #バトル終了後の処理

        while not i:

            if pyautogui.locateCenterOnScreen('result.png'):
            #リザルトＯＫを押す
                pyautogui.moveTo(305,583,1.8)
                time.sleep(0.4)
                pyautogui.click()
                time.sleep(0.4)
                if pyautogui.locateCenterOnScreen("classUp.png"):
                    ##キャラのＬＢ
                    time.sleep(0.6)
                    pyautogui.click()
                    time.sleep(0.6)
                    ##Limボーナス開放が足りないので追加
                    time.sleep(0.6)
                if pyautogui.locateCenterOnScreen("limbos.png"):
                    time.sleep(0.6)
                    pyautogui.moveTo(306,576,1.8)
                    pyautogui.click()

                time.sleep(0.6)
                if pyautogui.locateCenterOnScreen("LimBosclass.png"):
                    time.sleep(0.6)    ##キャラのLBコストＵＰ
                    pyautogui.moveTo(303,565,1.8)
                    pyautogui.click()
                    time.sleep(0.6)
                if pyautogui.locateCenterOnScreen("missionclear.png"):
                    time.sleep(0.6)    ##ミッションクリア
                    pyautogui.moveTo(277,766,1.8)
                    pyautogui.click()
                #一度ループを抜ける
                i = True
                            #もう一度挑戦する
                pyautogui.moveTo(200, 517, 1.8)
                pyautogui.click()



def button_actions():


    quest = quest_var.get()

    if quest == "業火の試練":
        yesno = messagebox.askyesno("確認", "業火の試練を周回しますか？")
        if yesno:

        #マイページランダムクリック
            time.sleep(1)
            webbrowser.open("http://game.granbluefantasy.jp/")

            time.sleep(0.5)
            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()
            time.sleep(0.5)

            #クエストクリック
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()
            time.sleep(0.5)

            #エクストラクリック
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()
            time.sleep(0.5)

            #属性クエストクリック
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()
            time.sleep(0.5)

            #業火の試練クリック
            pyautogui.moveTo(x_fire_random,y_fire_random, 2.0)
            pyautogui.click()
            time.sleep(0.5)
            AP_AA_FC()


    elif quest == "玉水の試練":
        yesno1 = messagebox.askyesno("確認", "玉水の試練を周回しますか？")

        if yesno1:
        #マイページランダムクリック
            time.sleep(1)
            webbrowser.open("http://game.granbluefantasy.jp/")

            time.sleep(0.5)
            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_water_random, y_water_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            AP_AA_FC()

    elif quest == "荒土の試練":
        yesno2 = messagebox.askyesno("確認", "荒土の試練を周回しますか？")
        if yesno2:
        #マイページランダムクリック
            time.sleep(0.5)
            webbrowser.open("http://game.granbluefantasy.jp/")

            time.sleep(0.5)
            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_sand_random, y_sand_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            AP_AA_FC()

    elif quest == "狂風の試練":
        yesno3 = messagebox.askyesno("確認", "狂風の試練を周回しますか？")
        if yesno3 == True:
        #マイページランダムクリック
            time.sleep(0.5)
            webbrowser.open("http://game.granbluefantasy.jp/")

            time.sleep(0.5)
            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_wind_random, y_wind_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            AP_AA_FC()

    elif quest == "極光の試練":
        yesno4 = messagebox.askyesno("確認", "極光の試練を周回しますか？")
        if yesno4 == True:
        #マイページランダムクリック
            time.sleep(0.5)

            webbrowser.open("http://game.granbluefantasy.jp/")
            time.sleep(0.5)

            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()
        #クエストクリック
            time.sleep(0.5)
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()
        #エクストラクリック
            time.sleep(0.5)
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_shine_random, y_shine_random, 2.0)
            pyautogui.click()
            time.sleep(0.5)

            AP_AA_FC()

    elif quest == "幽闇の試練":
        yesno5 = messagebox.askyesno("確認", "幽闇の試練を周回しますか？")
        if yesno5 == True:
        #マイページランダムクリック
            time.sleep(0.5)
            webbrowser.open("http://game.granbluefantasy.jp/")

            time.sleep(0.5)
            pyautogui.moveTo(x_mypage_random, y_mypage_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_quest_random, y_quest_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_extra_random, y_extra_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_zokuseiquest_random, y_zokuseiquest_random,2.0)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(x_dark_random, y_dark_random, 2.0)
            pyautogui.click()

            time.sleep(0.5)

            AP_AA_FC()
    else:
        messagebox.showerror("error", "不明なエラーが発生しました")

x_mypage_random = random.randint(213,389)

y_mypage_random = random.randint(714,748)

x_quest_random = random.randint(435,491)

y_quest_random = random.randint(521,595)

x_extra_random = random.randint(261,378)

y_extra_random = random.randint(504,524)

x_zokuseiquest_random = random.randint(398,514)

y_zokuseiquest_random = random.randint(806,823)

x_fire_random = random.randint(448,482)

y_fire_random = random.randint(370,400)

x_water_random = random.randint(449,478)

y_water_random = random.randint(444,473)

x_sand_random = random.randint(452,478)

y_sand_random = random.randint(517,551)

x_wind_random = random.randint(452,478)

y_wind_random = random.randint(595,625)

x_shine_random = random.randint(452,478)

y_shine_random = random.randint(671,703)

x_dark_random = random.randint(452,478)

y_dark_random = random.randint(747,773)

root = tk.Tk()

# ウインドウのタイトルを定義する
root.title(u'▼グラブル属性素材周回スクリプト▼')
# ここでウインドウサイズを定義する
root.geometry('400x300+700+350')
root.resizable(False,False)

quest_var = StringVar()

Static1 = tk.Label(root,text=u"属性素材クエスト",font=("MSゴシック", "10", "bold"))
Static1.place(x=20,y=5)

lbl = tk.Label(text='')
lbl1 = tk.Label(text='※50回以内に収めて１時間程度"休憩"停止してください')
text = "ブラウザを開くよ！！！"
radio_fire = ttk.Radiobutton(text="業火の試練",value="業火の試練",width=10,variable=quest_var)
radio_water = ttk.Radiobutton(text="玉水の試練",value="玉水の試練",width=10,variable=quest_var)
radio_sand = ttk.Radiobutton(text="荒土の試練",value="荒土の試練",width=10,variable=quest_var)
radio_wind = ttk.Radiobutton(text="狂風の試練",value="狂風の試練",width=10,variable=quest_var)
radio_shine = ttk.Radiobutton(text="極光の試練",value="極光の試練",width=10,variable=quest_var)
radio_darkness = ttk.Radiobutton(text="幽闇の試練",value="幽闇の試練",width=10,variable=quest_var)
aradio_darkness = ttk.Radiobutton(text="幽闇のa試練",value="幽a闇の試練",width=10,variable=quest_var)
entry = tk.Entry(width=5)
entry.place(x=200, y=70)
button1 = ttk.Button(
root,
text='OK',
command=button_actions)
radio_fire.place(x=20,y=30)
radio_water.place(x=20,y=50)
radio_sand.place(x=20,y=70)
radio_wind.place(x=20,y=90)
radio_shine.place(x=20,y=110)
radio_darkness.place(x=20,y=130)
aradio_darkness.place(x=20,y=150)
button1.place(x=160,y=250)
lbl.place(x=120, y=70)
lbl1.place(x=120, y=100)
a = entry.get()
##APがないときと召喚石選択リザルト画面OKからもう一度挑戦まで関数

root.mainloop()