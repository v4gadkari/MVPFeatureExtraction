from typing import final
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
sys.path.insert(0,'/usr/local/bin/chromedriver')
import pandas as pd 
import numpy as np 
import requests


from bs4 import BeautifulSoup

id_1 = 'mvp'
id_2 = 'nba_mvp'

r = requests.get('https://www.basketball-reference.com/awards/awards_2021.html')


soup = BeautifulSoup(r.text, 'html.parser')

    

table = soup.find('table', {'id':'mvp'})

thead = table.find('thead')
column_names = table.find_all('tr')

#h1s = table.find('h1')
#print(h1s)

table_row = column_names[1]

table_headers = table.find_all('th')

column_text = [item.text for item in table_headers]

column_text_final = column_text[1:]


rows = table.find_all('tr')

player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

final_player_stats = player_stats[2:]

column_text = column_text_final[6:25]

stats = pd.DataFrame(final_player_stats, columns=column_text)


stats.to_csv('2020_21_Season.csv')



"""

year=1956

all_dfs = []
h1_arr = []
df_lengths = []
for i in range(year, 2021):
    r = requests.get(f'https://www.basketball-reference.com/awards/awards_{i}.html')


    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', {'id':'mvp'})

    tbody = table.find('tbody')

    for item in tbody:
        data = item.find('tr').text()
        print(data)

    

"""
   



  

        



    #h1s = table.find('h1')
    #h1_arr.append(h1s.text)



    #columns = column_text_final[6:25]
    #stats = pd.DataFrame(final_player_stats, columns = column_text_final)
    #df_lengths.append(len(stats['Player']))


    #all_dfs.append(stats)
    



#years = []
#i = 0
#while i < len(h1_arr):
    #year = h1_arr[i]
    #length = df_lengths[i]
    #season = [year]*length
    #years.extend(season)
    #i+=1



    









    




#final_df = pd.concat(all_dfs)
#final_df = final_df.assign(Year = years)



#final_df.to_csv('mvp.csv')



#new_df = all_dfs[0].append(all_dfs[1], ignore_index=True)

#print(new_df)





#print(first_df)
#print(len(player_stats))
#print(len(column_text))

#print(final_player_stats[0])
    

#stats.to_csv('1954.csv')
#print(stats.head())


#df = pd.read_html('https://www.basketball-reference.com/awards/awards_1956.html')

#print(df)

#print(column_text)
