import time
from selenium import webdriver

# 自作処理
from commonFunc import classCommonFunc

class classLogin:
    def __init__(self, driver,mail,password): #コンストラクタ
        self.driver = driver
        self.mailAddress = mail
        self.password = password

        self.common = classCommonFunc()
        self.login()

    def login(self):
        # ログインしているかを判定
        if(self.IsLogin() == True):
            # 既にログイン済みなら処理終了
            print("ログイン済み")
            return

        # ログインしていない場合、ユーザのアイコンをクリック
        user_icon = self.driver.find_element_by_id('authIcon')
        user_icon.click()

        # ログイン画面が出るのを待機
        time.sleep(3)

        # メールアドレスとパスワードを設定してログインボタンを押す
        self.LoginSubmit()

        print("ログイン完了")

    # ユーザアイコンのsrcを参照し、ログイン完了済みかどうかを判定
    def IsLogin(self):
        userIcon = self.driver.find_element_by_class_name("userIcon")
        userIconSrc = userIcon.get_attribute("src")
        strCheck = "images/auth.png"    # ログイン未実施時のユーザアイコンのパス

        ret = self.common.ContainWord(userIconSrc,strCheck)
        if(ret == True):
            # 含む場合はログイン未実施
            ret = False
        else:
            # 含まない場合がログイン済み
            ret = True
        return ret

    # メールアドレスとパスワードを設定してログインボタンを押す
    def LoginSubmit(self):
        email = self.driver.find_element_by_id('login-email')
        password = self.driver.find_element_by_id('login-pass')
        loginButton = self.driver.find_element_by_id('login-button')

        email.send_keys(self.mailAddress)
        password.send_keys(self.password)
        loginButton.click()
        # ボタン押してからなんとなく待つ。
        time.sleep(1)