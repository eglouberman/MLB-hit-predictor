import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import csv
import re

def month(number):
    if number is "01":
        return "January"
    elif number is "02":
        return "February"
    elif number is "03":
        return "March"
    elif number is "04":
        return "April"
    elif number is "05":
        return "May"
    elif number is "06":
        return "June"
    elif number is "07":
        return "July"
    elif number is "08":
        return "August"
    elif number is "09":
        return "September"
    elif number is "10":
        return "October"
    elif number is "11":
        return "November"
    elif number is "12":
        return "December"

homepage1 = "https://www.baseball-reference.com/players/gl.fcgi?id="
homepage2 = "&t=p&year="
df = pd.read_csv("probable_pitchers.csv")
pitchers = pd.read_csv("pitchers.csv")
csv = open("stats.csv", "w+")
csv.write("Pitcher_ID,Year,Rank,Game_Number,Team_Game_Number,Date,Team,At,Opponent,Result,Innings,Decision,Days_Rest,Innings_Pitched,Hits_Allowed,Runs_Allowed,Earned_Runs_Allowed,Bases,Strikeouts,Home_Runs_Allowed,Times_Hit,ERA,Batters_Faced,Pitchers_in_PA,Strikes,Strikes_Looking,Strikes_Swinging,Ground_Balls,Fly_Balls,Line_Drives,Pop_Ups,Unknown_Batted_Ball_Type,Game_Score,Inherited_Runners,Inherited_Score,Stolen_Bases,Caught_Stealing,Pickoffs,At_Bats,Double_Hits_Allowed,Triple_Hits_Allowed,Intentional_Bases_on_Balls,Double_Plays_Grounded_Into,Sacrifice_Flies,Reached_on_Errors,Average_Leverage_Index,Win_Probability_Added,BaseOut_Runs_Saved,Entered,Exited\n")

for i in range(0, len(pitchers)):
    pitcherpage = homepage1 + pitchers.Pitcher_ID[i]
    try:
        pitcherhtml = urlopen(pitcherpage)
    except URLError as u:
        print(u)
    else:
        pitcherbs = BeautifulSoup(pitcherhtml, "html.parser")
        dateList = pitcherbs.find_all("a", {"href":re.compile("year=2")})
        dates = []
        for j in dateList:
            if len(j.get_text()) is 4 and j.get_text() not in dates and int(j.get_text()) > 2013:
                dates.append(j.get_text())
        for k in dates:
            homepage = homepage1 + pitchers.Pitcher_ID[i] + homepage2 + str(k)
            try:
                html = urlopen(homepage)
            except URLError as u:
                print(u)
            else:
                bs = BeautifulSoup(html, "html.parser")
                statList = bs.find_all("tr", {"id":re.compile("pitching_gamelogs")})
                for l in statList:
                    print(pitcherpage + " " + str(k))
                    csv.write(pitchers.Pitcher_ID[i] + "," + str(k) + ",")
                    for m in l:
                        print(m)
                        print(m.get_text())
                        csv.write(m.get_text() + ",")
                    csv.write("\n")



        #statList = bs.find_all("a", {"href": re.compile(df.Date[i][0:4] + df.Date[i][5:7] + df.Date[i][8:10])})


    """
    for j in eraList:
        print(j.parent.parent.find("td", {"data-stat":"earned_run_avg"}).get_text())
        csv.write(j.parent.parent.find("td", {"data-stat":"earned_run_avg"}).get_text() + ",")
    rivalEraList = rivalbs.find_all("a", {"href": re.compile(df.Date[i][0:4] + df.Date[i][5:7] + df.Date[i][8:10])})
    for k in rivalEraList:
        csv.write(k.parent.parent.find("td", {"data-stat": "earned_run_avg"}).get_text() + ",\n")
        """







