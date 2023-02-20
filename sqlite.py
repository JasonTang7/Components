# coding:utf-8

import sqlite3
import time
import datetime

class DB:
    # def __init__(self):
    #     self.Start()
    #     self.CreatTable()
    #     self.Close()
    #     print(self.id)

    def Start(self,path):
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
            (?, ?, ?, '0', '', '0', '10', '0', '30000', '30000', '5000', '0', '4800', '0', '15000', '0', '15000', '0', '0', '15', '0', '0', '0', '0', '0', '0', '-1', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0', '0');
            '''
            self.Start()
            self.cursor.execute(sql, (ID, RecipeName,datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))
            self.conn.commit()
            return 1
        except Exception as e:
            print('>> Insert Error:', e)
            return 0

    def Select(self, id):
        self.cursor.execute('''SELECT * from ocr WHERE id=(?);''', (id,))
        res = self.cursor.fetchall()
        return res

    def Close(self):
        self.cursor.close()
        self.conn.close()

    def SelectALL(self):
        sql = "SELECT * from WeldResult;"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def CheckContinuity(self):
        self.cursor.execute("select rowid, CycleCounter from WeldResult")
        lastCycle = -1
        lastID = -1
        for row in self.cursor:
            rowID = row[0]
            CycleNum = row[1]
            if(CycleNum != lastCycle + 1 and (CycleNum != 0) and (CycleNum != 1) and CycleNum != lastCycle):
                        print("previous:", lastID, lastCycle)
                        print("current:", rowID, CycleNum)
            lastCycle = CycleNum
            lastID = rowID

    def counter(self):
        counter = len(self.SelectALL())
        print(counter)

if __name__ == '__main__':
    path="C:/Users/E1397524/Desktop/db/sample_l20_base.db"
    db = DB()
    db.Start(path)
    # #Insert data
    # for i in range (1000):
    #     db.Insert(i+1,i+1)
    # # result=db.SelectALL()
    # # print(result)
    db.counter()
    db.CheckContinuity()
    db.Close()