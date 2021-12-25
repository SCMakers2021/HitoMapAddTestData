import pandas as pd

class ReadCsv:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath_or_buffer=filepath,encoding="cp932",sep=',')
        self.num = self.df.size
        self.len = len(self.df)

    def csvPrint(self):
        print("データ数：" + str(self.num))
        print(self.df)
        print(self.getLine(0,"コメント"))
        # self.getLine(0)
            
    def getLine(self,index,column):
        return self.df.at[index,column]

    def testWrite(self):
        data = {"美味しいお弁当です","心を込めて作りました"}
        df = pd.DataFrame(data)
        self.WriteCsv(df)

    def WriteCsv(self,df):
        df.to_csv('to_csv_out.csv')