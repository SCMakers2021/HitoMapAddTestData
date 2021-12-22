class classCommonFunc:
    #コンストラクタ省略

    #メソッド
    # 指定文字列が含まれるかをチェック
    def ContainWord(self,strSrc,strCheck):
        if strCheck in strSrc:
            ret = True
        else:
            ret = False

        return ret


