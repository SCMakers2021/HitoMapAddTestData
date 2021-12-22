import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from enum import IntEnum

# 自作処理
from commonFunc import classCommonFunc



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
        
    def ClickMap(self,MapPos):
        # アマリ投稿のフォームを開いているとクリックできない場合があるため、消す
        self.CloseAmariForm1()  

        # 指定座標をクリック
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element_with_offset(self.wholePage, self.MapPosArray[MapPos][0], self.MapPosArray[MapPos][1]).click().perform()

    # アマリ投稿のフォームを消す
    def CloseAmariForm1(self):
        # サガス→アマリの順に押すと消える
        self.ClickSagasuButton()
        self.ClickAmariButton()