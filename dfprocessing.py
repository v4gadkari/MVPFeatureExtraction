import pandas as pd





year = 1955
second_year = 1956
li=[]
year_lengths = []
while (year <= 2020 and second_year <= 2021):
    filename = str(year) + '_' + str(second_year) + '_' + 'Season.csv'
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
    year_length = len(df['Player']) #get lengths of player column to determine number of samples for given year
    year_lengths.append(year_length) # append to get lengths of each player column for each df
    year = int(year)
    second_year = int(second_year)
    year += 1
    second_year += 1



first_season = 1955
years = [(first_season) for first_season in range(first_season, 2021)]






seasons = []



i = 0
while i < len(years):
    date = years[i]
    length = year_lengths[i]
    season = [date]*length
    seasons.extend(season)
    i+=1



mvp_df = pd.concat(li, axis=0, ignore_index=True)

mvp_df['Year'] = seasons

mvp_df.to_csv('mvp_final.csv')
#df_lengths = [len(df['Player']) for df in li]

