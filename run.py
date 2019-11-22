import pandas as pd
import datetime
import config
import utils


count=0
def to_resoult(date,play_type,nums):
    
    data_dict={
        "种类":play_type,
        "日期":date,
        "平均数":utils.get_mean(nums),
        "中位数":utils.get_median(nums),
        "众数":utils.get_mode(nums)
    }
    data=pd.DataFrame(data_dict,index=[0])
    
    return data
#获得所有日期的列表
def init_during_date(start,last):
    dates=[]
    for num in  range(0,last):
        target_date=start+datetime.timedelta(days=num)
        dates.append(utils.get_str_date(target_date))
    return dates
def gudge_player(account_id,account_register_time,player_type_dict,battle_time,today,game_arr):
    for player_type in player_type_dict.keys():
        end=utils.get_datetime_by_str(today)+datetime.timedelta(player_type_dict[player_type]['条件'][1])
        start=utils.get_datetime_by_str(today)+datetime.timedelta(player_type_dict[player_type]['条件'][0])
        #print(str(int(account_register_time)))
        register=utils.get_datetime_by_str(str(int(account_register_time)))
        #print(register)
        if register>=start and register<=end:
            game_arr[player_type].append(battle_time)
            utils.log(str(account_id)+"属于"+str(player_type))
def get_secondary_player():
    pass
def init_games_arr(player_types):
    game_arr={}
    for player_type in player_types.keys():
        game_arr[player_type]=[]
    return game_arr

def handle_account_col(arr,player_type,today,game_arr):
    global count
    count+=1
    print(count)
    battle_times=arr['times']
    register_time=arr['register_time_wx2']
    if register_time=='no_data':
        return
    gudge_player(arr['#account_id'],register_time,player_type,battle_times,today,game_arr)

if __name__ == "__main__":
    start_date=datetime.datetime(2019,11,10)
    last_day=11
    player_type=config.get_config('config.json')['player_type']
    days=init_during_date(start_date,last_day)
    game_arr=init_games_arr(player_type)
    battle=pd.read_csv('data/battle.csv').fillna('no_data')
    recharge=pd.read_csv('data/recharge.csv')
    data=pd.DataFrame()
    for day in days:
        #当日的battle信息
        print(day)
        today_battle_date=utils.get_battle_time(day)
        today_battle=battle[battle['$part_date']==today_battle_date]
        print(len(today_battle))
        #遍历battle
        today_battle.apply(handle_account_col,axis=1,player_type=player_type,today=day,game_arr=game_arr)
        #保存player_type,并init
        utils.save_to_excel(str(day)+".xlsx",game_arr)
        
        for play_type in player_type:
            new_data=to_resoult(day,play_type,game_arr[play_type])
            print(new_data)
            data=data.append(new_data)
           
        game_arr=init_games_arr(player_type)
    data.to_excel("resoult.xlsx")    

    #print(get_str_date(date))