import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from enum import IntEnum
from datetime import datetime

# 自作処理
from commonFunc import classCommonFunc
from Category import Category


class MapPosition(IntEnum):
    LEFT_TOP = 0
    CENTER_TOP = 1
    RIGHT_TOP = 2
    LEFT_MIDDLE = 3
    CENTER_MIDDLE = 4
    RIGHT_MIDDLE = 5
    LEFT_BOTTOM = 6
    CENTER_BOTTOM = 7
    RIGHT_BOTTOM = 8

# アマリ登録の画面操作
class classAmariWindow:
    def __init__(self, driver): #コンストラクタ
        self.driver = driver
        self.common = classCommonFunc()
        self.wholePage = self.driver.find_element_by_id('map_canvas')
        
        WindowSize = driver.get_window_size()
        self.width = WindowSize['width']
        self.height = WindowSize['height']
        
        self.MapPosArray = [
            [self.width * 2/10,self.height * 2/10], # LEFT_TOP
            [self.width * 5/10,self.height * 2/10], # CENTER_TOP
            [self.width * 8/10,self.height * 2/10], # RIGHT_TOP
            [self.width * 2/10,self.height * 5/10], # LEFT_MIDDLE
            [self.width * 5/10,self.height * 5/10], # CENTER_MIDDLE
            [self.width * 8/10,self.height * 5/10], # RIGHT_MIDDLE
            [self.width * 2/10,self.height * 7/10], # LEFT_BOTTOM
            [self.width * 5/10,self.height * 7/10], # CENTER_BOTTOM
            [self.width * 8/10,self.height * 7/10]  # RIGHT_BOTTOM
        ]

    # アマリボタンを押す
    def ClickAmariButton(self):
        AamariButton = self.driver.find_element_by_id('btnAmari')
        AamariButton.click()

    # サガスボタンを押す
    def ClickSagasuButton(self):
        SagasuButton = self.driver.find_element_by_id('btnSagasu')
        SagasuButton.click()
        
    # 地図をクリックして投稿の画面を出す
    def ClickMap(self,MapPos):
        # アマリ投稿のフォームを開いているとクリックできない場合があるため、消す
        self.CloseAmariForm1()  

        # 指定座標をクリック
        # いきなりクリックするとサガスの吹き出しが邪魔になる場合があるため、右→左とおしてから押したい場所をクリックする
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element_with_offset(self.wholePage, self.MapPosArray[MapPosition.RIGHT_MIDDLE][0], self.MapPosArray[MapPosition.RIGHT_MIDDLE][1]).click().perform()    # 右
        time.sleep(0.5)
        actionChains.move_to_element_with_offset(self.wholePage, self.MapPosArray[MapPosition.LEFT_MIDDLE][0], self.MapPosArray[MapPosition.LEFT_MIDDLE][1]).click().perform()    # 左
        time.sleep(0.5)
        actionChains.move_to_element_with_offset(self.wholePage, self.MapPosArray[MapPos][0], self.MapPosArray[MapPos][1]).click().perform()

    # アマリ投稿のフォームを消す
    def CloseAmariForm1(self):
        # サガス→アマリの順に押すと消える
        self.ClickSagasuButton()
        self.ClickAmariButton()

    # 投稿ボタンを押す
    def ClickPostButton(self):
        PostButton = self.driver.find_element_by_id('PostButton')
        PostButton.click()

    # カテゴリを設定
    def SetCategoryList(self,Category):
        categoryList = self.driver.find_element_by_id('category')
        select = Select(categoryList) # ③ Selectオブジェクト生成
        # カテゴリを設定
        select.select_by_value(Category.optionvalue) 

    # 期限を設定
    def SetDeadTime(self,deadtime):
        deadtimeStr = datetime.strftime(deadtime, '%Y/%m/%d')
        year = datetime.strftime(deadtime, '%Y')
        month = datetime.strftime(deadtime, '%m')
        date = datetime.strftime(deadtime, '%d')
        deadTimeList = self.driver.find_element_by_id('deadTime')
        deadTimeList.clear()
        # deadTimeList.send_keys(deadtimeStr)
        deadTimeList.send_keys(year)          # 年
        deadTimeList.send_keys(Keys.TAB)    # TAB
        deadTimeList.send_keys(month)       # 月
        deadTimeList.send_keys(date)        # 日

    # コメントを設定
    def SetComment(self,Category):
        comment = self.driver.find_element_by_id('comment')
        comment.clear()
        comment.send_keys(Category.Comment)

    # 写真を設定
    def SetImg(self,Category):
        PicButton = self.driver.find_element_by_id('AmariPic')
        print(Category.imgPath)
        PicButton.send_keys(Category.imgPath)

    # 投稿する
    def Post(self,Category,deadtime):
        # カテゴリのデータを投稿画面に設定
        self.SetCategoryData(Category,deadtime)
        time.sleep(1)
        # 「次へ」ボタンを押す
        self.ClickNextButton()
        time.sleep(1)
        # 確定ボタンを押す
        self.ClickSubmitButton()
        time.sleep(5)

    # 次へボタンを押す
    def ClickNextButton(self):
        NextButton = self.driver.find_element_by_id('amariNext')
        NextButton.click()

    # 確定ボタンを押す
    def ClickSubmitButton(self):
        SubmitButton = self.driver.find_element_by_id('amariSubmit')
        SubmitButton.click()

    # カテゴリのデータを投稿画面に設定
    def SetCategoryData(self,Category,deadtime):
        # カテゴリを設定
        self.SetCategoryList(Category)
        # 日付を設定
        self.SetDeadTime(deadtime)
        # コメントを設定
        self.SetComment(Category)
        # 写真を設定
        self.SetImg(Category)

    
    # 場所を移動
    def MovePosition(self,StrArea):
        serachInput = self.driver.find_element_by_id('search-text')
        serachInput.clear()
        serachInput.send_keys(StrArea)
        serachInput.send_keys(Keys.ENTER)   # Enterキーを押して移動する
        time.sleep(1)
        print(StrArea + "に移動")