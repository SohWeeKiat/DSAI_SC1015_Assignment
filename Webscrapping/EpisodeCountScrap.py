import pandas as pd
from AnimeDataRow import AnimeDataRow

df = pd.read_csv('anime_data_combined.csv')
df['episodes'] = df['episodes'].astype('str')

for index,row in df.iterrows():
	if row['episodes'] == '0':
		temp = AnimeDataRow(row['rank'], row['title'], row['score'], row['url'])
		df.at[index,'episodes'] = str(temp.QueryEpisodes())
		if df.at[index,'episodes'] == '0':
			df.at[index,'episodes'] = pd.NA
df.to_csv("anime_data_combined_v2.csv")
