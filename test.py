import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 自作処理呼び出し
from commonFunc import classCommonFunc
from login import classLogin
from AmariWindow import classAmariWindow,MapPosition
from Category import Category

# common = classCommonFunc()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://master.d3s8lj7u41imf0.amplifyapp.com/')

# # アマリボタンを押す
# AmariWindow = classAmariWindow(driver)
# # AmariWindow.ClickAmariButton()

# # 投稿先へ移動
# for pos in MapPosition:
#     AmariWindow.ClickMap(pos)
#     print(pos)
#     time.sleep(2)

# # 投稿

# # search_box = driver.find_element_by_name("q")
# # search_box.send_keys('ChromeDriver')
# # search_box.submit()
# time.sleep(5)
# driver.quit()

# categoryBento = Category("お弁当","0","comment/お弁当/お弁当Comment.csv","\img\お弁当")
categoryBento = Category("お弁当","0","comment\お弁当\お弁当Comment.csv","\img\お弁当")
# categoryBento.setRandamComment()
print(categoryBento.Comment)
categoryBento.setRamdamData()
print(categoryBento.imgPath)