import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import os 


#pip install pytrends 



def write_data_to_csv(search_terms,start_year,start_month,start_day, end_year,end_month,end_day):
    return "".join(search_terms) + str(start_year) + str(start_month) + str(start_day) + str(end_year)+str(end_month)+str(end_year)



cwd=os.getcwd()
google_data_path = cwd+"\\GOOGLE_TRENDS_DATA\\"
if(not os.path.exists(google_data_path)):
    os.mkdir(google_data_path)


pytrend = TrendReq()
search_terms=['New York Knicks']
pytrend.build_payload(kw_list=search_terms)


#Start Year
start_year=2016
start_month=10
start_day=1

#End Year
end_year=2018
end_month=4
end_day=20


file_name = write_data_to_csv(search_terms,start_year,start_month,start_day, end_year,end_month,end_day)
interest_over_time_hourly = pytrend.get_historical_interest(search_terms, year_start=start_year, month_start=start_month, day_start=start_day, year_end=end_year, month_end=end_month, day_end=end_day)

interest_over_time_hourly.to_csv(google_data_path + file_name+".csv")
#interest_over_time_full_past = pytrend.interest_over_time()


print("The full interest over time full past is ")
print(interest_over_time_hourly)

