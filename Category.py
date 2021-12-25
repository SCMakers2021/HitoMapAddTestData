import os
from ReadCsv import ReadCsv
import random

class Category:
    def __init__(self, categoryName,optionvalue,CommentPath,imgFolderPath):
        self.categoryName = categoryName
        self.Comment = ""
        self.optionvalue = optionvalue
        self.CommentPath = CommentPath
        self.imgFolderPath = os.getcwd() + imgFolderPath
        self.imgPath = ""
        self.csv = ReadCsv(CommentPath)
        self.imgList = self.getImgList()
        # コメントと画像パスを設定する
        self.setRamdamData()

    def setRamdamData(self):
        self.setRandamComment()
        self.setRandamImgPath()

    def setRandamComment(self):
        ran = random.randint(0,self.csv.len-1)
        self.Comment = self.csv.getLine(ran,"コメント")
        # print("ran：" + str(ran))
        # print("len：" + str(self.csv.len))
        # print(self.Comment)

    def getImgList(self):
        files = os.listdir(self.imgFolderPath)
        # print(files)
        return files

    def setRandamImgPath(self):
        ran = random.randint(0,len(self.imgList)-1)
        self.imgPath = self.imgFolderPath + '/' + self.imgList[ran]