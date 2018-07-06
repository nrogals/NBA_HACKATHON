import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os 
import pandas as pd 


#pip install pytrends 

def write_data_to_csv(search_terms,start_year,start_month,start_day, end_year,end_month,end_day):
    return "".join(search_terms) + str(start_year) + str(start_month) + str(start_day) + str(end_year)+str(end_month)+str(end_year)


cwd=os.getcwd()
google_data_path = cwd+"\\GOOGLE_TRENDS_DATA\\"
if(not os.path.exists(google_data_path)):
    os.mkdir(google_data_path)

basket_ball_teams= ["Boston Celtics","Brooklyn Nets", "New York Knicks", "Philadelphia 76ers", "Toronto Raptors", "Chicago Bulls", "Cleveland Cavaliers",
"Detroit Pistons", "Indiana Pacers", "Milwaukee Bucks", "Atlanta Hawks", "Charlotte Hornets", "Miami Heat", "Orlando Magic", "Washington Wizards", "Denver Nuggets", "Minnesota Timberwolves", 
"Oklahoma City Thunder", "Portland Trail Blazers", "Utah Jazz", "Golden State Warriors", "Los Angeles Clippers", "Los Angeles Lakers", "Phoenix Suns", "Sacramento Kings", "Dallas Mavericks", 
"Houston Rockets", "Memphis Grizzlies", "New Orleans Pelicans", "San Antonio Spurs"]

#Begin Year 
start_year=2018
start_month=4
start_day=1
#End Year
end_year=2018
end_month=4
end_day=20


pytrend = TrendReq()
#Check for the existence of the data 
for basketball_team in basket_ball_teams:
    search_terms=[basketball_team]
    
    
    #Start Year
    file_name = write_data_to_csv(search_terms,start_year,start_month,start_day, end_year,end_month,end_day)
    if(not os.path.exists(google_data_path + file_name+".csv")):
        pytrend.build_payload(kw_list=search_terms)
        interest_over_time_hourly = pytrend.get_historical_interest(search_terms, year_start=start_year, month_start=start_month, day_start=start_day, year_end=end_year, month_end=end_month, day_end=end_day)
        interest_over_time_hourly.to_csv(google_data_path + file_name+".csv")
        print("Pasing First")

#Get the training data 


#Get the data path
cwd=os.getcwd()
data_path=cwd +"\\Business Analytics\\Business Analytics\\Business Analytics\\"
training_data = pd.read_csv(data_path+ "training_set.csv")
split_idx = int(len(training_data)*.8)
training_data = training_data[:split_idx]
test = training_data[split_idx:]



team_symbol_dict = \
{
"Atlanta Hawks" : "ATL",\
"Brooklyn Nets" : "BKN",\
"Boston Celtics" : "BOS",\
"Charlotte Hornets" : "CHA",\
"Chicago Bulls" : "CHI",\
"Cleveland Cavaliers" : "CLE",\
"Dallas Mavericks" : "DAL",\
"Denver Nuggets" : "DEN",\
"Detroit Pistons" : "DET",\
"Golden State Warriors" : "GSW",\
"Houston Rockets" : "HOU",\
"Indiana Pacers" : "IND",\
"Los Angeles Clippers" : "LAC",\
"Los Angeles Lakers" : "LAL",\
"Memphis Grizzlies" : "MEM",\
"Miami Heat" : "MIA",\
"Milwaukee Bucks" : "MIL",\
"Minnesota Timberwolves" : "MIN",\
"New Orleans Pelicans" : "NOP",\
"New York Knicks" : "NYK",\
"Oklahoma City Thunder" : "OKC",\
"Orlando Magic" : "ORL",\
"Philadelphia 76ers" : "PHI",\
"Phoenix Suns" : "PHX",\
"Portland Trail Blazers" : "POR",\
"Sacramento Kings" : "SAC",\
"San Antonio Spurs" : "SAS",\
"Toronto Raptors" : "TOR",\
"Utah Jazz" : "UTA",\
"Washington Wizards" : "WAS"
}

symbol_team_dict =  {v: k for k, v in team_symbol_dict.items()}


#print(dictionary)



print(training_data.columns)


#print((training_data.loc[ training_data['Home_Team']=='NYK' or  training_data['Home_Team']=='CLE']  )) 
#assert(1<0)

#Collect the data team_pandas_veiwership

#print(team_pandas_veiwership)

for basket_ball_abreviation in list(symbol_team_dict.keys()):
    team_pandas_veiwership = pd.concat( [training_data.loc[ training_data['Home_Team']=='NYK'], training_data.loc[ training_data['Away_Team']=='NYK']] ) 
    val = team_pandas_veiwership["Rounded Viewers"].idxmax()
    max = team_pandas_veiwership["Rounded Viewers"].max()
    team_pandas_veiwership.to_csv("Veiwership_CSV.csv")


    print("The values of max and idx max are respectively: ")
    print(max)
    print(val)

    print("The row of the index is: ")
    print((training_data.iloc[val])["Game_Date"])
    print(type(training_data.iloc[val]))
    



    assert(1<0)



"""
search_term=[basketball_team]
file_name = write_data_to_csv(search_terms,start_year,start_month,start_day, end_year,end_month,end_day)
df= pd.read_csv(google_data_path + file_name + ".csv")
print(df.loc[df['Home_Team']=='NYK'])
"""
