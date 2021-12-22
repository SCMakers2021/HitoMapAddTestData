from commonFunc import classCommonFunc

common = classCommonFunc()

strSrc = "https://master.d3s8lj7u41imf0.amplifyapp.com/images/auth.png"
strCheck = "images/auth.png"


ret = common.ContainWord(strSrc,strCheck)
print(ret)
