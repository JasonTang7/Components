import sqlite3

# '''创建一个数据库，文件名'''
# 如果给定的数据库名称 filename 不存在，则该调用将创建一个数据库
conn = sqlite3.connect(r"C:\Users\E1397524\Desktop\db\20221027\sample_l20_base.db")
# '''创建游标'''
cursor = conn.cursor()

# # 判断sqlite数据库中的表是否存在，不存在就创建
# try:
#     create_tb_cmd='''
#     CREATE TABLE IF NOT EXISTS k_trace_log
#     (ExecID varchar(64),
#     ObjectID varchar(64),
#     sTime varchar(20),
#     sMsg varchar(256));
#     '''
#     #主要就是上面的语句 : CREATE TABLE IF NOT EXISTS USER
#     cursor.execute(create_tb_cmd)
# except:
#     print("Create table failed")


# 插入信息
# insert_tb_cmd = '''INSERT INTO "main"."WeldRecipe" ("ID", "RecipeName", "DateTime", "UserID", "PresetPicPath", "IsValidate", "Amplitude", "Width", "WeldPressure", "TriggerPressure", "TimePlus", "TimeMinus", "PeakPowerPlus", "PeakPowerMinus", "TriggerHeightPlus", "TriggerHeightMinus", "WeldHeightPlus", "WeldHeightMinus", "WeldMode", "ModeValue", "PreBurst", "HoldTime", "SqueezeTime", "AfterBurstDelay", "AfterBurstDuration", "AfterBurstAmplitude", "StepWeldMode", "EnergyToStep", "TimeToStep", "PowerToStep", "WeldHeight", "MeasuredHeight") VALUES ('8', '3', '1900/07/00 08:06:00', '0', '', '0', '10', '0', '30000', '30000', '5000', '0', '4800', '0', '15000', '0', '15000', '0', '0', '0', '0', '0', '0', '0', '0', '0', '-1', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0', '0')'''

for i in range(1000):
    # 执行语句
    cursor.execute('''INSERT INTO "main"."WeldRecipe" VALUES ('1','1', '2022/10/28 08:06:00', '0', '', '0', '10', '0', '30000', '30000', '5000', '0', '4800', '0', '15000', '0', '15000', '0', '0', '0', '0', '0', '0', '0', '0', '0', '-1', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0,0,0;0,0,0;0,0,0;0,0,0;0,0,0;', '0', '0')''')
# 事务提交 
conn.commit()    




# # 查询所有的信息
# select_tb_cmd = '''select * from k_trace_log '''
# # 执行语句
# results = cursor.execute(select_tb_cmd)
# # 遍历打印输出
# all_logs = results.fetchall()
# for log in all_logs:
#     print(log)