import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 自作処理呼び出し
from login import classLogin

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://master.d3s8lj7u41imf0.amplifyapp.com/')

# ページ表示時に待機
time.sleep(3)

# ログインする
mail = "ita-dtc2021@scnet.co.jp"
password = "ita-DTC2021@"
login = classLogin(driver,mail,password)

# 投稿先へ移動

# 投稿

# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
time.sleep(5)
driver.quit()