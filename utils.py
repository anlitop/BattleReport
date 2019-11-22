import pandas as pd
import datetime
import numpy as np
from scipy import stats

def save_to_excel(file,kdict):
    with pd.ExcelWriter(file) as writer: 
        for kname in kdict.keys():
            pd.DataFrame(kdict[kname]).to_excel(writer,sheet_name=kname)
def log(content):
    with open ("log.csv",'a') as f :
        f.write(str(datetime.datetime.now())+"  "+content+'\n')
#处理/的日期,返回一个str类型的日期
def get_battle_time(battle_date):  
    return battle_date[0:4]+'/'+battle_date[4:6]+'/'+battle_date[6:8]
#传入一个str类型的日期返回datetime
def get_datetime_by_str(str_date):
    #20191011
    year=int(str_date[0:4])
    month=int(str_date[4:6])
    day=int(str_date[6:8])
    return datetime.datetime(year,month,day)
#将datetime类型时间转为年月日的str表示
def get_str_date(date):
    year=date.year
    month=date.month
    day=date.day
    return str(year)+str(month)+str(day)
    
def get_mean(nums):
    return np.mean(nums)
def get_median(nums):
    return np.median(nums)
def get_mode(nums):
    return stats.mode(nums)[0][0]


