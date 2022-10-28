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

    def Start(self, path='sql.db'):
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

    def Insert(self, user, score):
        try:
            sql = '''
            INSERT INTO ocr ( id, user, score, update_date )
            VALUES
            (NULL, ?, ?, ?);
           '''
            self.Start()
            self.cursor.execute(sql, (user, score, datetime.datetime.now()))
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
    db.Insert('1', '4')
    res = db.SelectALL()
    print(res)