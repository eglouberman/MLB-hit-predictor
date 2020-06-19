from statcast_batter import statcast_batter
from baseball_scraper import playerid_lookup
import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import re
import pickle


def append_next_game_details(df2):
    #determine if the player gets a hit the next game
    df_huge = pd.DataFrame()
    player_names= list(df2["Name"].unique())
    for name in player_names:
        df_player = df2[df2["Name"] == name]
        df_p = df_player.sort_values(by = ["fixed_date"])
        df_p["next_game_BA"] = df_p["BA"].shift(-1)
        df_p["next_game_Name"] = df_p["Name"].shift(-1)
        df_p["next_game_Date"] = df_p["fixed_date"].shift(-1)
        df_p["next_game_Key"] = df_p["key"].shift(-1)
        df_huge = pd.concat([df_huge, df_p], axis = 0)
    return df_huge


def calculate_next_game_stats(next_game_df):
    df = next_game_df.copy()
    df['TB'] = [1 if 'single' == str(df['events'][x]) else 2 if 'double' == str(df['events'][x]) else 3 if 'triple' == str(df['events'][x]) else 4 if 'home_run' == str(df['events'][x]) else 0 for x in range(len(df))]
    df['walk'] = [1 if 'walk' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['SF'] = [1 if 'sac_fly' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['HBP'] = [1 if 'hit_by_pitch' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['out'] = [1 if 'out' in str(df['events'][x]) or 'grounded' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['hit'] = [1 if 'single' in str(df['events'][x]) or 'home_run' in str(df['events'][x]) or 'double' == str(df['events'][x]) or 'triple' == str(df['events'][x]) else 0 for x in range(len(df))]
    df['AB'] = [0 if len(str(df['events'][x])) < 4 or df['walk'][x] or 'sac' in str(df['events'][x]) or df['HBP'][x] or 'catcher' in str(df['events'][x]) else 1 for x in range(len(df))]
    df['HR'] = [1 if 'home_run' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['HIP'] =[1 if 'into_play' in str(df["description"][x]) else 0 for x in range(len(df))]    #basic stats. Keep in mind that it is a little off because there are no IBB accounted for. 
    num_walks  = df["walk"].sum()
    num_hits = df['hit'].sum()
    num_AB = df['AB'].sum()

    next_game_hit = 0
    if (num_hits > 0):
        next_game_hit = 1

    first_pitcher_faced_id = df.sort_values(by="inning").iloc[0]["pitcher"]

    num_hits_against_pitcher = df[df["pitcher"] == first_pitcher_faced_id]['hit'].sum()
    num_ABs_against_pitcher = df[df["pitcher"] == first_pitcher_faced_id]['AB'].sum()
    inning_faced_first = df.sort_values(by="inning").iloc[0]["inning"]

    stats = { "next_game_date" : [df["game_date"][0]], "HomeTeam": [df["home_team"][0]], "AwayTeam": [df["away_team"][0]], "Walks_next_game": [num_walks], "H_total_next_game" :[num_hits], "next_game_HIT": [next_game_hit],"AB_next_game": [num_AB],
             "first_pitcher_faced_next_game_id": [first_pitcher_faced_id], "hits_vs_first_pitcher": [num_hits_against_pitcher],
            "AB_vs_first_pitcher": [num_ABs_against_pitcher], "earliest_inning": [inning_faced_first]}

    return pd.DataFrame.from_dict(stats)

def find_aggregate_hitting_stats(last_name, first_name, start_time, end_time, my_dict):
    #function that finds aggregate stats for a hitter for given start and end times
    
    sries = (first_name, last_name)
    if (sries in my_dict):
        lookup_id = my_dict[(first_name,last_name)]
    else:
        # stats = {"Name": [first_name + ' ' + last_name], "Game_date": [end_time]}
        # calc = pd.DataFrame.from_dict(stats)[list(stats.keys())]
        return pd.DataFrame()
    try:
        main_df = statcast_batter(start_time, end_time,lookup_id)
    except:
        stats = {"Name": [first_name + ' ' + last_name], "Game_date": [end_time]}
        calc = pd.DataFrame.from_dict(stats)[list(stats.keys())]
        print("couldn't get ", first_name, last_name)
        return pd.DataFrame()
    #likely that the player didn't play in this year
    if(len(main_df) ==0):
        return pd.DataFrame()
    main_df = main_df[main_df["game_type"] == "R"] #limit to regular season

    main_df["date"] = pd.to_datetime(main_df.game_date)
    all_dates_in_season = list(main_df["date"].unique())
    all_dates_in_season.reverse()
    main_df = main_df.sort_values(by = ["date"]).set_index("date")

    if (len(main_df) == 1):
        return pd.DataFrame()

    begin = main_df.index[0]

    final_df = pd.DataFrame()
    curr_index = 0
    for date in all_dates_in_season:
        df = main_df[begin:date].copy()
        df = df.reset_index()
        # don't include sacrifices
        df['TB'] = [1 if 'single' == str(df['events'][x]) else 2 if 'double' == str(df['events'][x]) else 3 if 'triple' == str(df['events'][x]) else 4 if 'home_run' == str(df['events'][x]) else 0 for x in range(len(df))]
        df['walk'] = [1 if 'walk' in str(df['events'][x]) else 0 for x in range(len(df))]
        df['SF'] = [1 if 'sac_fly' in str(df['events'][x]) else 0 for x in range(len(df))]
        df['HBP'] = [1 if 'hit_by_pitch' in str(df['events'][x]) else 0 for x in range(len(df))]
        df['out'] = [1 if 'out' in str(df['events'][x]) or 'grounded' in str(df['events'][x]) else 0 for x in range(len(df))]
        df['hit'] = [1 if 'single' in str(df['events'][x]) or 'home_run' in str(df['events'][x]) or 'double' == str(df['events'][x]) or 'triple' == str(df['events'][x]) else 0 for x in range(len(df))]
        df['AB'] = [0 if len(str(df['events'][x])) < 4 or df['walk'][x] or 'sac' in str(df['events'][x]) or df['HBP'][x] or 'catcher' in str(df['events'][x]) else 1 for x in range(len(df))]
        df['HR'] = [1 if 'home_run' in str(df['events'][x]) else 0 for x in range(len(df))]
        df['HIP'] =[1 if 'into_play' in str(df["description"][x]) else 0 for x in range(len(df))]
        #basic stats. Keep in mind that it is a little off because there are no IBB accounted for. 
        num_SF = df["SF"].sum()
        num_HBP = df["HBP"].sum()
        num_walks  = df["walk"].sum()
        num_hits = df['hit'].sum()
        num_outs = df['out'].sum()
        num_AB = df['AB'].sum()
        num_TB = df["TB"].sum()
        num_HR = df["HR"].sum()
        games_in_range = len(df["game_date"].unique())
        game_date = date


        PA = df["events"].count()
        batting_average = num_hits/(num_hits + num_outs)
        OBP = (num_hits + num_walks + num_HBP)/(num_AB + num_walks + num_HBP + num_SF)
        SLG = num_TB/(num_AB)
        OPS = SLG + OBP
        ISO = SLG-batting_average
        LA_avg = df["launch_angle"].dropna().mean()
        LA_median = df["launch_angle"].dropna().median()
        bip = len(df[df['HIP'] ==1])/num_AB #bip  / number of AB
        babip_df = df[df['HIP'] == 1]
        babip = (babip_df["hit"].sum() - num_HR)/(len(babip_df)-num_HR)

        """
        If we want to keep track of streaky players, this information could be very useful.
        """
        ten_days_stats = pd.DataFrame()
        twenty_days_stats = pd.DataFrame()
        thirty_days_stats = pd.DataFrame()
        #last 10 games
        if (games_in_range >=10):
            new_begin = all_dates_in_season[curr_index - 9]
            pass_df = main_df[new_begin:date].copy()
            pass_df = pass_df.reset_index()
            ten_days_stats =get_stats_from_window(pass_df, 10)

        #last 20 games
        if (games_in_range >=20):
            new_begin = all_dates_in_season[curr_index - 19]
            pass_df = main_df[new_begin:date].copy()
            pass_df = pass_df.reset_index()
            twenty_days_stats =get_stats_from_window(pass_df, 20)

        #last 30 games
        if (games_in_range >=30):
            new_begin = all_dates_in_season[curr_index - 29]
            pass_df = main_df[new_begin:date].copy()
            pass_df = pass_df.reset_index()
            thirty_days_stats =get_stats_from_window(pass_df, 30)

        
        """
        Calculate next game stats
        """
        next_game_stats = pd.DataFrame()
        if (curr_index +1 < len(all_dates_in_season)):
            next_games_date =all_dates_in_season[curr_index +1]
            next_game_df = main_df[main_df.index == next_games_date].copy()
            next_game_stats = calculate_next_game_stats(next_game_df)

        
        #find ratio of type of pitch when got a hit to total hits
        df_hits = df[df["hit"] ==1]
        df_summary = df_hits.groupby("pitch_type").sum() 
        df_summary["percentage_of_total_hits"] = df_summary["hit"]/num_hits
        col_names = [x + "_percentage_hits" for x in df_summary.index]
        percentage_hits_df = pd.DataFrame([df_summary["percentage_of_total_hits"].values],columns = col_names)

        #find zone success percentage
        df_sum = df_hits.groupby("zone").sum()
        df_sum["percentage_of_zones"] = df_sum["hit"]/num_hits
        col_names = ["pHitsByZone" + str(int(x)) for x in df_sum.index]
        zone_df = pd.DataFrame([df_sum["percentage_of_zones"].values], columns = col_names)
        
        #launch_speed_angle calculation out of total plate appearances (6  options)
        df_sum = pd.DataFrame(df["launch_speed_angle"].value_counts())
        for r in range(1,7):
            if (r not in df_sum.index):
                df_sum = df_sum.append(pd.Series([0], index=df_sum.columns, name=r))
        df_sum["percentage_of_lsa"] = df_sum["launch_speed_angle"]/df_sum["launch_speed_angle"].sum()
        types = ["Weak", "Topped", "Under", "Flare/Burner", "SolidContact", "Barrel"]
        col_names = [str(x) + "_lsa_p" for x in types]
        lsa_df = pd.DataFrame([df_sum["percentage_of_lsa"].values], columns = col_names)
        df["launch_speed_angle"].unique()
        # except:
        #     lsa_df = pd.DataFrame(np.array([np.nan for x in range(len(col_names))]).reshape(1,6), columns = col_names)

        stats = {"Name": [first_name + ' ' + last_name], "Game_date": [game_date], "Games_played_to_date": [games_in_range],
                    "mlbam_code": [lookup_id], "PA": [PA], "Walks": [num_walks],
                    "BA": [batting_average], "OBP": [OBP], "SLG": [SLG], "OPS": [OPS], "ISO": [ISO], 
                    "LA_avg": [LA_avg], "LA_median": [LA_median], "BIP": [bip], "BABIP": [babip]}

        # print(my_dict)
        calc = pd.DataFrame.from_dict(stats)
        final_row = pd.concat([calc,percentage_hits_df,zone_df, lsa_df, ten_days_stats, twenty_days_stats, thirty_days_stats, next_game_stats], axis=1, sort = False)
        final_df = pd.concat([final_df, final_row], axis = 0, sort = False)
        curr_index +=1
    return final_df

# function that returns stats for a given window frame
def get_stats_from_window(df, window):
    df['TB'] = [1 if 'single' == str(df['events'][x]) else 2 if 'double' == str(df['events'][x]) else 3 if 'triple' == str(df['events'][x]) else 4 if 'home_run' == str(df['events'][x]) else 0 for x in range(len(df))]
    df['walk'] = [1 if 'walk' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['SF'] = [1 if 'sac_fly' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['HBP'] = [1 if 'hit_by_pitch' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['out'] = [1 if 'out' in str(df['events'][x]) or 'grounded' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['hit'] = [1 if 'single' in str(df['events'][x]) or 'home_run' in str(df['events'][x]) or 'double' == str(df['events'][x]) or 'triple' == str(df['events'][x]) else 0 for x in range(len(df))]
    df['AB'] = [0 if len(str(df['events'][x])) < 4 or df['walk'][x] or 'sac' in str(df['events'][x]) or df['HBP'][x] or 'catcher' in str(df['events'][x]) else 1 for x in range(len(df))]
    df['HR'] = [1 if 'home_run' in str(df['events'][x]) else 0 for x in range(len(df))]
    df['HIP'] =[1 if 'into_play' in str(df["description"][x]) else 0 for x in range(len(df))]
    #basic stats. Keep in mind that it is a little off because there are no IBB accounted for. 
    num_SF = df["SF"].sum()
    num_HBP = df["HBP"].sum()
    num_walks  = df["walk"].sum()
    num_hits = df['hit'].sum()
    num_outs = df['out'].sum()
    num_AB = df['AB'].sum()
    num_TB = df["TB"].sum()
    num_HR = df["HR"].sum()
    games_in_range = len(df["game_date"].unique())

    PA = df["events"].count()
    batting_average = num_hits/(num_hits + num_outs)
    OBP = (num_hits + num_walks + num_HBP)/(num_AB + num_walks + num_HBP + num_SF)
    SLG = num_TB/(num_AB)
    OPS = SLG + OBP
    ISO = SLG-batting_average
    LA_median = df["launch_angle"].dropna().median()
    bip = len(df[df['HIP'] ==1])/num_AB #bip  / number of AB
    babip_df = df[df['HIP'] == 1]
    babip = (babip_df["hit"].sum() - num_HR)/(len(babip_df)-num_HR)
    
    stats = {"PA_last_%i_games"% window: [PA], "Walks_last_%i_games"% window: [num_walks],
                    "BA_last_%i_games"% window: [batting_average], "OBP_last_%i_games"% window: [OBP], 
                     "SLG_last_%i_games"% window: [SLG], "OPS_last_%i_games"% window: [OPS], "ISO_last_%i_games"% window: [ISO], 
                     "LAmed_last_%i_games"% window: [LA_median], "BIP_last_%i_games"% window: [bip], "BABIP_last_%i_games"% window: [babip]}
    return pd.DataFrame.from_dict(stats)


def main():
    #get my_dict
    my_dict = {}
    with open("data/mydict.pickle", 'rb') as handle:
        my_dict = pickle.load(handle)
    # Give the location of the file 
    loc = ("data/GameLogs_1419.csv") 
    # To open Workbook 
    df = pd.read_csv(loc)


    df["Date"] = [x[0:10] for x in df["Date"]]
    df['Date'] = df['Date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d'))

    start_time = datetime.now()
    df_big = pd.DataFrame()

    #df_big = pd.read_csv("data/aggregates.csv")
    if (len(df_big > 0)):
        already_in_there = df_big["Name"].unique()
    else:
        already_in_there = []
    d = {}
    for item in already_in_there:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    total = len(my_dict)
    count = len(d)

    for keys in my_dict:
        print("Getting info for..." + keys[0] + ' ' + keys[1])
        check  = keys[0] +' '+ keys[1]
        if (check in d or keys[0] =="Adalberto"):
            continue
        years = [2014,2015,2016,2017,2018,2019]
        for year in years:
            first_name = keys[0]
            last_name= keys[1]
            first_date = str(year) + '-03-01'
            second_date = str(year) + '-11-01'
            df_player = find_aggregate_hitting_stats(last_name, first_name, first_date, second_date, my_dict)
            if (len(df_big.columns) ==0):
                df_big = pd.concat([df_big, df_player], axis = 1, sort = False)
            else:
                df_big = pd.concat([df_big, df_player], axis = 0, sort = False)
            next_time = datetime.now()
            delta = next_time - start_time
            
            if delta.seconds > 180: # we back up every 3 minutes
                print("uploading backup to a csv file.....")
                try:
                    df_big.to_csv("Data/aggregates.csv", index = False)
                except:
                    df_big.to_csv("Data/aggregates2.csv", index = False)
                start_time = next_time
        try:
            p_done = 100*(count/total)
            if (int(p_done)% 5 ==0):
                print("Finished with..." + str(p_done) + "%")
        except:
            pass
        count +=1


    # df = df.reset_index()
    # for row,col in df.iterrows():
    #     row = df.iloc[row]
    #     player_name = row["Player"]
    #     first_name = re.findall('(.*) ', player_name)[0]
    #     #if the name has a '.' in it like "A.J."
    #     if (first_name[1] =='.'):
    #         first_name = first_name[:2] + ' ' + first_name[2:]
    #     last_name = re.findall('.* (.*)\\\\', player_name)[0]
    #     first_year = row["Date"].year
    #     first_date = str(first_year) + '-03-01'
    #     second_date = str(row["Date"])[:10]
    #     print("player: ", first_name + " " + last_name)
    #     df_player = find_aggregate_hitting_stats(last_name, first_name, first_date, second_date, my_dict)
    #     if (len(df_big.columns) ==0):
    #         df_big = pd.concat([df_big, df_player], axis = 1, sort = False)
    #     else:
    #         df_big = pd.concat([df_big, df_player], axis = 0, sort = False)
        # next_time = datetime.now()
        # delta = next_time - start_time
        # if delta.seconds > 10: # we back up every 15 minutes
        #     print("uploading backup to a csv file.....")
        #     try:
        #         df_big.to_csv("Data/aggregates.csv", index = False)
        #     except:
        #         df_big.to_csv("Data/aggregates2.csv", index = False)
        #     start_time = next_time
    df_big.to_csv("aggregates.csv", index = False)
    


if __name__ == '__main__':
    main()