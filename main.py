import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime,timedelta
import random

# 自作処理呼び出し
from login import classLogin
from AmariWindow import classAmariWindow,MapPosition
from Category import Category
from AreaList import AreaList

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://master.d3s8lj7u41imf0.amplifyapp.com/')

# ページ表示時に待機
time.sleep(3)

# ログインする
mail = "ita-dtc2021@scnet.co.jp"
password = "ita-DTC2021@"
login = classLogin(driver,mail,password)

# 投稿データを設定
categoryBento = Category("お弁当","0","comment/お弁当/お弁当Comment.csv","/img/お弁当")
categoryCake = Category("ケーキ","1","comment/ケーキ/ケーキComment.csv","/img/ケーキ")
categorySushi = Category("寿司","2","comment/お寿司/お寿司Comment.csv","/img/お寿司")
categoryBurger = Category("ハンバーガー","3","comment/ハンバーガー/ハンバーガーComment.csv","/img/ハンバーガー")
today = datetime.today()
# deadtime = today + timedelta(days=7)    # 1週間後
deadtimeBase = today + timedelta(days=37)    # 今日

# アマリボタンを押す
AmariWindow = classAmariWindow(driver)
AmariWindow.ClickAmariButton()

# 投稿先へ移動
areList = AreaList()
for area in areList.List:
    AmariWindow.MovePosition(area)
    for pos in MapPosition:
        try:
            ran = random.randint(0,3)
            ran2 = random.randint(0,10)
            deadtime = deadtimeBase + timedelta(days=ran2)    # 今日
            if(ran == 0):
                category = categoryBento
            elif(ran == 1):
                category = categoryCake
            elif(ran == 2):
                category = categorySushi
            else:
                category = categoryBurger
            AmariWindow.ClickMap(pos)
            # 投稿データを切り替え
            category.setRamdamData()
            # 投稿
            # 投稿ボタンを押す
            time.sleep(1)
            AmariWindow.ClickPostButton()
            # 投稿データを設定して投稿する
            AmariWindow.Post(category,deadtime)
        except Exception as e:
            print(e)
            time.sleep(3)


time.sleep(5)
driver.quit()
