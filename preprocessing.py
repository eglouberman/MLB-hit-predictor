from sklearn.preprocessing import LabelBinarizer, StandardScaler
import pandas as pd
import numpy as np

class Preprocess():
    def __init__(self, df, add_weather_encoder = True,  add_venue_encoder = True, add_wind_encoder = True, add_player_encoder = True):
        self.add_weather_encoder = add_weather_encoder
        self.add_venue_encoder = add_venue_encoder
        self.add_wind_encoder = add_wind_encoder
        self.add_player_encoder = add_player_encoder
        self.size = len(df)
        self.dataframe = df
    def encode_classes(self):
        encoder = LabelBinarizer()
        if self.add_weather_encoder:
            weather = self.dataframe["Weather Type"]
            encoded_weather = encoder.fit_transform(weather)
            weather_df = pd.DataFrame(encoded_weather, columns = encoder.classes_)
            self.dataframe = pd.concat([self.dataframe, weather_df], axis=1, sort = False, ignore_index = False)
        if self.add_venue_encoder:
            venue = self.dataframe["Venue"]
            encoded_venue = encoder.fit_transform(venue)
            venue_df = pd.DataFrame(encoded_venue, columns = encoder.classes_)
            self.dataframe = pd.concat([self.dataframe, venue_df], axis=1, sort = False, ignore_index = False)
        if self.add_wind_encoder:
            wind = self.dataframe["Wind Direction"]
            encoded_wind = encoder.fit_transform(wind)
            wind_df = pd.DataFrame(encoded_wind, columns = encoder.classes_)
            self.dataframe = pd.concat([self.dataframe, wind_df], axis=1, sort = False, ignore_index = False)
        if self.add_player_encoder:
            player = self.dataframe["Name"]
            encoded_player = encoder.fit_transform(player)
            player_df = pd.DataFrame(encoded_player, columns = encoder.classes_)
            self.dataframe = pd.concat([self.dataframe, player_df], axis=1, sort = False, ignore_index = False)
        if (len(self.dataframe) != self.size):
            raise Exception("Mistake in how we merged the new encoded classes!")
        return self.dataframe
    
    def clean_columns(self):
        #function removes these types of things in the dataset
        """
        - players that have played less than 15 games that season and that do not start the next game (earliest inning is less than 3)
        - categorical columns (like Date, name, park, venue, etc.)
        - categorical columns that are over 60 percent NaN
        """
        self.dataframe = self.dataframe[(self.dataframe["Games_played_to_date"] > 30) & (self.dataframe.earliest_inning <=3)].reset_index(drop=True)
        dates = self.dataframe["Game_date"] # we want to keep the date so that we can apply train test split according to the date
        other_columns_to_delete = ["Unnamed: 0", "Rank", "next_game_HIT",	"H_total_next_game", "AB_next_game", "Walks_next_game", "AB_vs_first_pitcher", 
                                   "earliest_inning", "hits_vs_first_pitcher","mlbam_code", "first_pitcher_faced_next_game_id", 
                                   "Games_played_to_date", "Year_x", "Year_y", "Team 1 Score", "Team 2 Score"]
        categorical_feature_columns = list(set(self.dataframe.columns) - set(self.dataframe._get_numeric_data().columns))
        
        cleaned = self.dataframe.drop(columns = categorical_feature_columns+other_columns_to_delete)
        cleaned2= pd.concat([dates,cleaned], axis = 1, sort = False, ignore_index= False)
        
        no_nans = self.drop_nans(cleaned2, 15) #any column with more than 30 percent nans will be deleted

        #get rid of the columns with more than 50 percent nans
        
        return no_nans

    def drop_nans(self, merge, limit):
        df_nans = merge.isna().sum()/len(merge)*100
        to_keep = []
        for x in range(len(df_nans)):
            if (df_nans[x] < limit):
                to_keep.append(df_nans.index[x])   
        df_no_nans = merge[to_keep]
        return df_no_nans

    def normalize(self, df):
        scaler = StandardScaler()
        scaler.fit(df.values)
        print(scaler.mean_)
        return scaler.transform(df.values)


def balance_hits(df_cleaned, target = "next_game_hit_vs_fp"):
    num_samples = min(df_cleaned[target].value_counts()[0],df_cleaned[target].value_counts()[1]) # where target = 0
    hits_indices = df_cleaned[df_cleaned[target]==1].index
    non_hits_indices =df_cleaned[df_cleaned[target]==0].index

    if (len(hits_indices) > len(non_hits_indices)):
        random_indices = np.random.choice(hits_indices, num_samples, replace = False)
        all_indices_to_keep = sorted(list(random_indices)+ list(non_hits_indices))
        cleaned_again = df_cleaned.loc[all_indices_to_keep].reset_index(drop=True)
    else:
        random_indices = np.random.choice(non_hits_indices, num_samples, replace = False)
        all_indices_to_keep = sorted(list(random_indices)+ list(hits_indices))
        cleaned_again = df_cleaned.loc[all_indices_to_keep].reset_index(drop=True)
    # print(cleaned_again[target].value_counts())
    return cleaned_again

def get_scaled_df_for_player(name, df):
    
    data = df[df[name]==1].dropna(axis=0).reset_index(drop=True)
    stats = ['PABABIP_combined', 'Clear', 'Cloudy', 'Dome', 'Drizzle', 'Overcast', 'weather_t',
    'Partly Cloudy', 'Rain', 'Roof Closed', 'Sunny', 'clear', 'Angel Stadium', 'Busch Stadium', 'Chase Field', 
    'Citi Field', 'Citizens Bank Park', 'Comerica Park', 'Coors Field', 'Dodger Stadium', 'Fenway Park', 
    'Great American Ball Park', 'Guaranteed Rate Field', 'Kauffman Stadium', 'Marlins Park', 'Miller Park', 
    'Minute Maid Park', 'Nationals Park', 'Oracle Park', 'Oriole Park at Camden Yards', 'PNC Park', 'Petco Park', 
    'Progressive Field', 'Rogers Centre', 'T-Mobile Park', 'Target Field', 'Tropicana Field', 'Truist Park', 
    'Wrigley Field', 'Yankee Stadium', 'Calm', 'In From CF', 'In From LF', 'In From RF', 'L To R', 'None', 
    'Out To CF', 'Out To LF', 'Out To RF', 'R To L', 'Varies', 'none','RUNS_norm', 'HR_norm', 'H_norm', '2B_norm', 
    '3B_norm', 'BB_norm', 'LF_outfield_norm', 'SLF_outfield_norm', 'LFA_outfield_norm', 'LCF_outfield_norm', 'LCC_outfield_norm', 
    'CF_outfield_norm', 'RCC_outfield_norm', 'RCF_outfield_norm', 'RFA_outfield_norm', 'SRF_outfield_norm', 'RF_outfield_norm', 
    'LF_wall_norm', 'LCF_wall_norm', 'CF_wall_norm', 'RCF_wall_norm', 'RF_wall_norm', 'Area_norm', 'Back_norm',
    'pHitsByZone4', 'pHitsByZone5', 'pHitsByZone8','hitter_R%', "next_game_hit_vs_fp", 'ground_ball_percentage','fly_ball_percentage',
    'strikeout_percentage', "ERA", "hip_season", "hip_last_five", "hip_last_three", "whip_season", "ppa_z"]
    for j in stats:
        if (j not in data.columns):
            print(j, "Does not exist")
    to_balance = data[stats]
    cleaned_again = balance_hits(to_balance)
    return cleaned_again



"""
ppa_z, PABIBP, strikeout percentage, hip season, ground ball percentage ()
ppa_z, PABIBP, strikeout percentage, hip last three, ground ball percentage ()

"""