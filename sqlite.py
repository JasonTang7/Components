# coding:utf-8

import sqlite3
import time
import datetime

class DB:
    def __init__(self):
        self.Start()
        self.CreatTable()
        self.Close()
        # print(self.id)

    def Start(self,path="C:/Users/E1397524/Desktop/db/20221027/sample_l20_base.db"):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def CreatTable(self):
        try:
            sql = '''
            CREATE TABLE IF NOT EXISTS `ocr`(
               `id` INTEGER PRIMARY KEY,
               `user` VARCHAR(100) NOT NULL,
               `score` INTEGER UNSIGNED NOT NULL,
               `update_date` TIMESTAMP
            );
            '''
            self.cursor.execute(sql)
            return 1
        except Exception as e:
            print('>> Creat Error:', e)
            return 0

    def Insert(self, ID, RecipeName):
        try:
            sql = '''
            INSERT INTO "main"."WeldRecipe" 
            ("ID", "RecipeName", "DateTime", "UserID", "PresetPicPath", "IsValidate", "Amplitude", "Width", "WeldPressure", "TriggerPressure", "TimePlus", "TimeMinus", "PeakPowerPlus", "PeakPowerMinus", "TriggerHeightPlus", "TriggerHeightMinus", "WeldHeightPlus", "WeldHeightMinus", "WeldMode", "ModeValue", "PreBurst", "HoldTime", "SqueezeTime", "AfterBurstDelay", "AfterBurstDuration", "AfterBurstAmplitude", "StepWeldMode", "EnergyToStep", "TimeToStep", "PowerToStep", "WeldHeight", "MeasuredHeight") 
            VALUES 
            (?, ?, ?, '0', '', '0', '10', '0', '30000', '30000', '5000', '0', '4800', '0', '15000', '0', '15000', '0', '0', '0', '0', '0', '0', '0', '0', '0', '-1', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0', '0');
            '''
            self.Start()
            self.cursor.execute(sql, (ID, RecipeName,datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
            self.conn.commit()
            self.Close()
            return 1
        except Exception as e:
            print('>> Insert Error:', e)
            return 0

    def Select(self, id):
        self.Start()
        self.cursor.execute('''SELECT * from ocr WHERE id=(?);''', (id,))
        res = self.cursor.fetchall()
        self.Close()
        return res

    def Close(self):
        self.cursor.close()
        self.conn.close()

    def SelectALL(self):
        self.Start()
        sql = "SELECT * from ocr;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.Close()
        return res


if __name__ == '__main__':
    db = DB()
    for i in range (1000):
        db.Insert(i+1,i+1)
